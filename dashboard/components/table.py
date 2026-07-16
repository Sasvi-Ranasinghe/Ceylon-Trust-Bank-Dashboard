from dash import dash_table
from utils.data_loader import load_data

# Load data first
data = load_data()

# Then extract DataFrames
customers = data["customers"]
transactions = data["transactions"]
accounts = data["accounts"]
loans = data["loans"]

def recent_transactions_table(province="ALL"):
    print("Province:", province)
    df = transactions.copy()

    if province != "ALL":
        customer_ids = customers[
            customers["Province"] == province
            ]["CustomerID"]

        account_numbers = accounts[
            accounts["CustomerID"].isin(customer_ids)
        ]["AccountNo"]

        df = df[
            df["AccountNo"].isin(account_numbers)
        ]

    df = df.sort_values(
        by="TransactionDate",
        ascending=False
    ).head(10)


    df["Amount"] = df["Amount"].apply(
        lambda x: f"LKR {x:,.2f}"
    )

    df["BalanceAfter"] = df["BalanceAfter"].apply(
        lambda x: f"LKR {x:,.2f}"
    )

    return dash_table.DataTable(

        columns=[
            {"name": i, "id": i}
            for i in df.columns
        ],

        data=df.to_dict("records"),

        style_as_list_view=True,

        style_header={

            "backgroundColor": "#1F3557",

            "color": "white",

            "fontFamily": "Consolas",

            "fontSize": "16px",

            "border": "none"

        },

        style_cell={

            "backgroundColor": "#16263F",

            "color": "white",

            "padding": "12px",

            "textAlign": "center",

            "border": "none",

            "fontSize": "14px",

            "fontWeight": "normal"

        },

        style_table={

            "overflowX": "auto"

        },

        page_size=10

    )

def top_accounts_table():

    df = (
        accounts
        .sort_values("Balance", ascending=False)
        .head(10)
    )
    df["Balance"] = df["Balance"].apply(lambda x: f"LKR {x:,.0f}")

    df = df[[
        "AccountNo",
        "CustomerID",
        "AccountType",
        "BranchName",
        "Balance",
        "Status"
    ]]

    return dash_table.DataTable(

        columns=[
            {"name": i, "id": i}
            for i in df.columns
        ],

        data=df.to_dict("records"),

        style_as_list_view=True,

        style_header={
            "backgroundColor": "#1F3557",
            "color": "white",
            "fontWeight": "bold"
        },

        style_cell={
            "backgroundColor": "#16263F",
            "color": "white",
            "padding": "10px",
            "textAlign": "center"
        },

        page_size=10
    )

def top_loans_table():

    df = (

        loans

        .sort_values("LoanAmount", ascending=False)

        .head(10)

    )

    df = df[[

        "LoanID",

        "CustomerID",

        "LoanType",

        "LoanAmount",

        "InterestRate",

        "LoanStatus"

    ]]

    df["LoanAmount"] = df["LoanAmount"].apply(

        lambda x: f"LKR {x:,.0f}"

    )

    return dash_table.DataTable(

        columns=[

            {"name": i, "id": i}

            for i in df.columns

        ],

        data=df.to_dict("records"),

        style_as_list_view=True,

        style_header={

            "backgroundColor":"#1F3557",

            "color":"white",

            "fontWeight":"bold"

        },

        style_cell={

            "backgroundColor":"#16263F",

            "color":"white",

            "padding":"10px",

            "textAlign":"center"

        },

        page_size=10

    )

loans = data["loans"]


def top_branches_table():

    df = (

        accounts.groupby("BranchName")
        .agg(

            Accounts=("AccountNo", "count"),
            TotalDeposits=("Balance", "sum"),
            AverageBalance=("Balance", "mean")

        )
        .reset_index()

        .sort_values(
            "TotalDeposits",
            ascending=False
        )

        .head(10)

    )

    df["TotalDeposits"] = df["TotalDeposits"].apply(
        lambda x: f"LKR {x:,.0f}"
    )

    df["AverageBalance"] = df["AverageBalance"].apply(
        lambda x: f"LKR {x:,.0f}"
    )

    return dash_table.DataTable(

        columns=[
            {"name": i, "id": i}
            for i in df.columns
        ],

        data=df.to_dict("records"),

        style_as_list_view=True,

        style_header={
            "backgroundColor": "#1F3557",
            "color": "white",
            "fontWeight": "bold"
        },

        style_cell={
            "backgroundColor": "#16263F",
            "color": "white",
            "padding": "10px",
            "textAlign": "center"
        },

        page_size=10

    )

def top_branches_chart():

    df = (

        accounts.groupby("BranchName")["Balance"]

        .sum()

        .reset_index()

        .sort_values(

            "Balance",

            ascending=False

        )

        .head(5)

    )

    fig = px.bar(

        df,

        x="Balance",

        y="BranchName",

        orientation="h",

        color="Balance",

        color_continuous_scale="Blues"

    )

    fig.update_layout(

        title="Top 5 Performing Branches",

        paper_bgcolor="#16263F",

        plot_bgcolor="#16263F",

        font_color="white",

        coloraxis_showscale=False,

        margin=dict(

            l=20,

            r=20,

            t=50,

            b=20

        )

    )

    return dcc.Graph(

        figure=fig,

        config={

            "displayModeBar": False

        }

    )
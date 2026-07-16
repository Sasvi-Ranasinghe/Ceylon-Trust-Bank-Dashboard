import pandas as pd
import plotly.express as px

from dash import dcc

from utils.data_loader import load_data

data = load_data()

accounts = data["accounts"]
transactions = data["transactions"]
loans = data["loans"]
customers = data["customers"]

def account_type_chart(province="ALL"):

    df = accounts.copy()

    if province != "ALL":

        customer_ids = customers[
            customers["Province"] == province
        ]["CustomerID"]

        df = df[
            df["CustomerID"].isin(customer_ids)
        ]

    df = df["AccountType"].value_counts().reset_index()

    df.columns = ["Account Type", "Count"]

    fig = px.pie(

        df,

        names="Account Type",

        values="Count",

        hole=0.60,

        color_discrete_sequence=[
            "#3B82F6",
            "#22C55E",
            "#D4AF37"
        ]

    )

    fig.update_layout(

        title="Account Type Distribution",

        paper_bgcolor="#16263F",

        plot_bgcolor="#16263F",

        font_color="white",

        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        )

    )

    return dcc.Graph(

        figure=fig,

        config={"displayModeBar": False}

    )

def monthly_account_opening_chart():

    df = accounts.copy()

    df["OpenDate"] = pd.to_datetime(df["OpenDate"])

    df["Month"] = df["OpenDate"].dt.strftime("%b")

    month_order = [
        "Jan","Feb","Mar","Apr","May","Jun",
        "Jul","Aug","Sep","Oct","Nov","Dec"
    ]

    monthly = (

        df.groupby("Month")
        .size()
        .reset_index(name="Accounts")

    )

    monthly["Month"] = pd.Categorical(

        monthly["Month"],

        categories=month_order,

        ordered=True

    )

    monthly = monthly.sort_values("Month")

    fig = px.line(

        monthly,

        x="Month",

        y="Accounts",

        markers=True

    )

    fig.update_traces(

        line_color="#3B82F6",

        line_width=4,

        marker_size=10

    )

    fig.update_layout(

        title="Monthly Account Openings",

        paper_bgcolor="#16263F",

        plot_bgcolor="#16263F",

        font_color="white",

        margin=dict(l=20,r=20,t=50,b=20)

    )

    return dcc.Graph(

        figure=fig,

        config={"displayModeBar":False}

    )

def loan_type_chart(province="ALL"):

    df = loans.copy()

    if province != "ALL":

        customer_ids = customers[
            customers["Province"] == province
        ]["CustomerID"]

        df = df[
            df["CustomerID"].isin(customer_ids)
        ]

    df = df["LoanType"].value_counts().reset_index()

    df.columns = ["Loan Type","Count"]

    fig = px.bar(

        df,

        x="Loan Type",

        y="Count",

        color="Count",

        color_continuous_scale="Blues"

    )

    fig.update_layout(

        title="Loan Portfolio",

        paper_bgcolor="#16263F",

        plot_bgcolor="#16263F",

        font_color="white",

        coloraxis_showscale=False

    )

    return dcc.Graph(

        figure=fig,

        config={"displayModeBar":False}

    )

def monthly_transaction_chart(province="ALL"):

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

    df["TransactionDate"] = pd.to_datetime(df["TransactionDate"])

    df["Month"] = df["TransactionDate"].dt.strftime("%b")

    monthly = (

        df.groupby("Month")["Amount"]

        .sum()

        .reset_index()

    )

    month_order = [

        "Jan","Feb","Mar","Apr","May","Jun",

        "Jul","Aug","Sep","Oct","Nov","Dec"

    ]

    monthly["Month"] = pd.Categorical(

        monthly["Month"],

        categories=month_order,

        ordered=True

    )

    monthly = monthly.sort_values("Month")

    fig = px.line(

        monthly,

        x="Month",

        y="Amount",

        markers=True

    )

    fig.update_traces(

        line_color="#3B82F6",

        line_width=4,

        marker_size=10

    )

    fig.update_layout(

        title="Monthly Transaction Trend",

        paper_bgcolor="#16263F",

        plot_bgcolor="#16263F",

        font_color="white",

        margin=dict(l=20,r=20,t=50,b=20)

    )

    return dcc.Graph(

        figure=fig,

        config={"displayModeBar":False}

    )

def transaction_channel_chart(province="ALL"):

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

    df = df["Channel"].value_counts().reset_index()

    df.columns = ["Channel","Count"]

    fig = px.pie(

        df,

        names="Channel",

        values="Count",

        hole=0.55,

        color_discrete_sequence=px.colors.sequential.Blues_r

    )

    fig.update_layout(

        title="Transaction Channels",

        paper_bgcolor="#16263F",

        plot_bgcolor="#16263F",

        font_color="white",

        margin=dict(l=20,r=20,t=50,b=20)

    )

    return dcc.Graph(

        figure=fig,

        config={"displayModeBar":False}

    )

def gender_chart():

    df = customers["Gender"].value_counts().reset_index()

    df.columns = ["Gender", "Count"]

    fig = px.pie(

        df,

        names="Gender",

        values="Count",

        hole=0.60,

        color_discrete_sequence=[
            "#3B82F6",
            "#EC4899"
        ]

    )

    fig.update_layout(

        title="Gender Distribution",

        paper_bgcolor="#16263F",

        plot_bgcolor="#16263F",

        font_color="white",

        margin=dict(l=20, r=20, t=50, b=20)

    )

    return dcc.Graph(

        figure=fig,

        config={"displayModeBar": False}

    )

def province_chart():

    df = customers["Province"].value_counts().reset_index()

    df.columns = ["Province", "Customers"]

    fig = px.bar(

        df,

        x="Customers",

        y="Province",

        orientation="h",

        color="Customers",

        color_continuous_scale="Blues"

    )

    fig.update_layout(

        title="Province Distribution",

        paper_bgcolor="#16263F",

        plot_bgcolor="#16263F",

        font_color="white",

        coloraxis_showscale=False,

        margin=dict(l=20, r=20, t=50, b=20)

    )

    return dcc.Graph(

        figure=fig,

        config={"displayModeBar": False}

    )

def occupation_chart():

    df = (
        customers["Occupation"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    df.columns = ["Occupation", "Count"]

    fig = px.bar(

        df,

        x="Occupation",

        y="Count",

        color="Count",

        color_continuous_scale="Blues"

    )
    fig.update_xaxes(tickangle=-30)

    fig.update_layout(

        title="Top 10 Occupations",

        paper_bgcolor="#16263F",

        plot_bgcolor="#16263F",

        font_color="white",

        coloraxis_showscale=False,

        margin=dict(l=20, r=20, t=50, b=20)

    )

    return dcc.Graph(

        figure=fig,

        config={"displayModeBar": False}

    )

def account_status_chart():

    df = accounts["Status"].value_counts().reset_index()

    df.columns = ["Status", "Count"]

    fig = px.bar(

        df,

        x="Status",

        y="Count",

        color="Status",

        color_discrete_sequence=[
            "#22C55E",
            "#F59E0B",
            "#EF4444"
        ]

    )

    fig.update_layout(

        title="Account Status",

        paper_bgcolor="#16263F",

        plot_bgcolor="#16263F",

        font_color="white",

        margin=dict(l=20, r=20, t=50, b=20),

        showlegend=False

    )

    return dcc.Graph(

        figure=fig,

        config={"displayModeBar": False}

    )

def average_balance_chart():

    df = (

        accounts.groupby("AccountType")["Balance"]

        .mean()

        .reset_index()

    )

    fig = px.bar(

        df,

        x="AccountType",

        y="Balance",

        color="Balance",

        color_continuous_scale="Blues"

    )

    fig.update_layout(

        title="Average Balance by Account Type",

        paper_bgcolor="#16263F",

        plot_bgcolor="#16263F",

        font_color="white",

        coloraxis_showscale=False,

        margin=dict(l=20,r=20,t=50,b=20)

    )

    return dcc.Graph(

        figure=fig,

        config={"displayModeBar":False}

    )

def deposit_withdrawal_chart():

    df = (
        transactions.groupby("TransactionType")["Amount"]
        .sum()
        .reset_index()
    )

    fig = px.bar(

        df,

        x="TransactionType",

        y="Amount",

        color="TransactionType",

        color_discrete_map={
            "Deposit": "#22C55E",
            "Withdrawal": "#EF4444"
        }

    )

    fig.update_layout(

        title="Deposits vs Withdrawals",

        paper_bgcolor="#16263F",

        plot_bgcolor="#16263F",

        font_color="white",

        showlegend=False

    )

    return dcc.Graph(

        figure=fig,

        config={"displayModeBar": False}

    )

def daily_transaction_chart():

    df = transactions.copy()

    df["TransactionDate"] = pd.to_datetime(df["TransactionDate"])

    daily = (
        df.groupby(df["TransactionDate"].dt.day_name())["Amount"]
        .sum()
        .reset_index()
    )

    day_order = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    daily["TransactionDate"] = pd.Categorical(
        daily["TransactionDate"],
        categories=day_order,
        ordered=True
    )

    daily = daily.sort_values("TransactionDate")

    fig = px.line(

        daily,

        x="TransactionDate",

        y="Amount",

        markers=True

    )

    fig.update_traces(

        line_color="#3B82F6",

        line_width=4,

        marker_size=8

    )

    fig.update_layout(

        title="Daily Transaction Volume",

        paper_bgcolor="#16263F",

        plot_bgcolor="#16263F",

        font_color="white",

        margin=dict(l=20, r=20, t=50, b=20)

    )

    return dcc.Graph(

        figure=fig,

        config={"displayModeBar": False}

    )

def loan_status_chart():

    df = loans["LoanStatus"].value_counts().reset_index()

    df.columns = ["Loan Status", "Count"]

    fig = px.bar(

        df,

        x="Loan Status",

        y="Count",

        color="Loan Status",

        color_discrete_map={

            "Active": "#22C55E",

            "Completed": "#3B82F6",

            "Defaulted": "#EF4444"

        }

    )

    fig.update_layout(

        title="Loan Status",

        paper_bgcolor="#16263F",

        plot_bgcolor="#16263F",

        font_color="white",

        showlegend=False,

        margin=dict(l=20,r=20,t=50,b=20)

    )

    return dcc.Graph(

        figure=fig,

        config={"displayModeBar":False}

    )

def loan_portfolio_chart():

    df = (

        loans

        .groupby("LoanType")["LoanAmount"]

        .sum()

        .reset_index()

    )

    fig = px.bar(

        df,

        x="LoanType",

        y="LoanAmount",

        color="LoanAmount",

        color_continuous_scale="Blues"

    )

    fig.update_layout(

        title="Loan Type Distribution",

        paper_bgcolor="#16263F",

        plot_bgcolor="#16263F",

        font_color="white",

        coloraxis_showscale=False,

        margin=dict(l=20,r=20,t=50,b=20)

    )

    return dcc.Graph(

        figure=fig,

        config={"displayModeBar":False}

    )

def interest_rate_chart():

    df = (

        loans

        .groupby("LoanType")["InterestRate"]

        .mean()

        .reset_index()

    )

    fig = px.bar(

        df,

        x="LoanType",

        y="InterestRate",

        color="InterestRate",

        color_continuous_scale="Teal"

    )
    fig.update_xaxes(
        tickangle=-30
    )

    fig.update_layout(

        title="Average Interest Rate",

        paper_bgcolor="#16263F",

        plot_bgcolor="#16263F",

        font_color="white",

        coloraxis_showscale=False,

        margin=dict(l=20,r=20,t=50,b=20)

    )

    return dcc.Graph(

        figure=fig,

        config={"displayModeBar":False}

    )

def branch_customer_chart():

    df = (
        accounts.groupby("BranchName")["CustomerID"]
        .count()
        .reset_index()
    )

    df.columns = ["Branch", "Customers"]

    fig = px.bar(
        df,
        x="Branch",
        y="Customers",
        color="Customers",
        color_continuous_scale="Blues"
    )

    fig.update_xaxes(tickangle=-35)

    fig.update_layout(
        title="Customers by Branch",
        paper_bgcolor="#16263F",
        plot_bgcolor="#16263F",
        font_color="white",
        coloraxis_showscale=False
    )

    return dcc.Graph(
        figure=fig,
        config={"displayModeBar": False}
    )

def branch_deposit_chart():

    df = (
        accounts.groupby("BranchName")["Balance"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        df,
        x="BranchName",
        y="Balance",
        color="Balance",
        color_continuous_scale="Blues"
    )

    fig.update_xaxes(tickangle=-35)

    fig.update_layout(
        title="Total Deposits by Branch",
        paper_bgcolor="#16263F",
        plot_bgcolor="#16263F",
        font_color="white",
        coloraxis_showscale=False
    )

    return dcc.Graph(
        figure=fig,
        config={"displayModeBar": False}
    )

def branch_account_chart():

    df = (
        accounts["BranchName"]
        .value_counts()
        .reset_index()
    )

    df.columns = ["Branch", "Accounts"]

    fig = px.bar(

        df,

        x="Branch",

        y="Accounts",

        color="Accounts",

        color_continuous_scale="Blues"

    )

    fig.update_xaxes(
        tickangle=-35
    )

    fig.update_layout(

        title="Account Distribution",

        paper_bgcolor="#16263F",

        plot_bgcolor="#16263F",

        font_color="white",

        coloraxis_showscale=False

    )

    return dcc.Graph(

        figure=fig,

        config={"displayModeBar":False}

    )

def province_branch_chart():

    df = (
        customers["Province"]
        .value_counts()
        .reset_index()
    )

    df.columns = ["Province", "Customers"]

    fig = px.pie(

        df,

        names="Province",

        values="Customers",

        hole=0.55,

        color_discrete_sequence=px.colors.sequential.Blues_r

    )

    fig.update_traces(

        textposition="inside",

        textinfo="percent",

        hovertemplate="<b>%{label}</b><br>Customers: %{value}<extra></extra>"

    )

    fig.update_layout(

        title="Province Distribution",

        paper_bgcolor="#16263F",

        plot_bgcolor="#16263F",

        font_color="white",

        margin=dict(l=20,r=20,t=60,b=20),

        legend=dict(

            orientation="v",

            y=0.5,

            yanchor="middle",

            x=1.05,

            xanchor="left",

            font=dict(size=11)

        )

    )

    return dcc.Graph(

        figure=fig,

        config={"displayModeBar":False},

        style={"height":"430px"}

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

    fig.update_traces(

        texttemplate="LKR %{x:,.0f}",

        textposition="inside",

        insidetextanchor="middle",

        textfont=dict(

            color="Black",

            size=13

        )

    )

    return dcc.Graph(

        figure=fig,

        config={

            "displayModeBar": False

        }

    )
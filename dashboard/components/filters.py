from dash import html, dcc
from utils.data_loader import load_data

data = load_data()

customers = data["customers"]
accounts = data["accounts"]
loans = data["loans"]


def create_filters():

    provinces = sorted(customers["Province"].unique())
    account_types = sorted(accounts["AccountType"].unique())
    loan_types = sorted(loans["LoanType"].unique())

    return html.Div(

        [

            dcc.Dropdown(

                id="province-filter",

                options=[{"label": "📍 All Provinces", "value": "ALL"}] +
                        [{"label": p, "value": p} for p in provinces],

                value="ALL",

                placeholder="Select Province",

                clearable=False,

                searchable=True,

                style={
                    "color": "black",
                    "width": "250px"},

                className="filter-dropdown"

            ),

            dcc.Dropdown(

                id="account-filter",

                options=[{"label": "💳 All Account Types", "value": "ALL"}] +
                [{"label": a, "value": a} for a in account_types],

                value="ALL",

                clearable=False,

                style={
                    "color": "black",
                    "width": "250px"},

                className="filter-dropdown"

            ),

            dcc.Dropdown(

                id="loan-filter",

                options=[{"label": "🏦 All Loan Types", "value": "ALL"}] +
                [{"label": l, "value": l} for l in loan_types],

                value="ALL",

                clearable=False,

                style={
                    "color": "black",
                    "width": "250px"},

                className="filter-dropdown"

            )

        ],

        className="filter-row"

    )

print(customers["Province"].unique())

print(accounts["AccountType"].unique())

print(loans["LoanType"].unique())
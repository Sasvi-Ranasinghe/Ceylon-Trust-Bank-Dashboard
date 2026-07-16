import dash
from dash import html

from utils.data_loader import load_data

from components.layout import chart_row

from components.charts import (

    account_type_chart,

    account_status_chart,

    monthly_account_opening_chart,

    average_balance_chart

)

from components.table import top_accounts_table

dash.register_page(
    __name__,
    path="/accounts",
    name="Accounts"
)

data = load_data()

accounts = data["accounts"]

layout = html.Div(

    [

        html.H1(
            "💳 Accounts Analytics",
            className="page-title"
        ),

        html.P(
            "Account portfolio analysis and banking performance",
            className="page-subtitle"
        ),

        # ===========================
        # KPI CARDS
        # ===========================

        html.Div(

            [

                html.Div(

                    [

                        html.H3("Total Accounts"),

                        html.H1(f"{len(accounts):,}")

                    ],

                    className="dashboard-card"

                ),

                html.Div(

                    [

                        html.H3("Savings Accounts"),

                        html.H1(

                            len(
                                accounts[
                                    accounts["AccountType"] == "Savings"
                                ]
                            )

                        )

                    ],

                    className="dashboard-card"

                ),

                html.Div(

                    [

                        html.H3("Current Accounts"),

                        html.H1(

                            len(
                                accounts[
                                    accounts["AccountType"] == "Current"
                                ]
                            )

                        )

                    ],

                    className="dashboard-card"

                ),

                html.Div(

                    [

                        html.H3("Fixed Deposits"),

                        html.H1(

                            len(
                                accounts[
                                    accounts["AccountType"] == "Fixed Deposit"
                                ]
                            )

                        )

                    ],

                    className="dashboard-card"

                )

            ],

            className="card-container"

        ),

        # ===========================
        # CHARTS
        # ===========================

chart_row(

    account_type_chart(),

    account_status_chart()

),

chart_row(

    monthly_account_opening_chart(),

    average_balance_chart()

),

html.Div(

    [

        html.H3(
            "Top 10 Highest Balance Accounts",
            className="section-title"
        ),

        top_accounts_table()

    ],

    className="table-card"

),
        ]
)
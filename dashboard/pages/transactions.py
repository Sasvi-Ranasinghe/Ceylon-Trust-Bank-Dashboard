import dash
from dash import html

from utils.data_loader import load_data

from components.layout import chart_row
from components.table import recent_transactions_table

from components.insights import transaction_insight_card

from components.charts import (
    monthly_transaction_chart,
    transaction_channel_chart,
    deposit_withdrawal_chart,
    daily_transaction_chart
)

dash.register_page(
    __name__,
    path="/transactions",
    name="Transactions"
)

data = load_data()

transactions = data["transactions"]

layout = html.Div(

    [

        html.H1(
            "💸 Transactions Analytics",
            className="page-title"
        ),

        html.P(
            "Transaction monitoring and payment behaviour",
            className="page-subtitle"
        ),

        # ===========================
        # KPI CARDS
        # ===========================

        html.Div(

            [

                html.Div(

                    [

                        html.H3("Total Transactions"),

                        html.H1(f"{len(transactions):,}")

                    ],

                    className="dashboard-card"

                ),

                html.Div(

                    [

                        html.H3("Deposits"),

                        html.H1(

                            len(

                                transactions[
                                    transactions["TransactionType"]=="Deposit"
                                ]

                            )

                        )

                    ],

                    className="dashboard-card"

                ),

                html.Div(

                    [

                        html.H3("Withdrawals"),

                        html.H1(

                            len(

                                transactions[
                                    transactions["TransactionType"]=="Withdrawal"
                                ]

                            )

                        )

                    ],

                    className="dashboard-card"

                ),

                html.Div(

                    [

                        html.H3("Average Transaction"),

                        html.H1(

                            f"LKR {transactions['Amount'].mean():,.0f}"

                        )

                    ],

                    className="dashboard-card"

                )

            ],

            className="card-container"

        ),

        chart_row(

            monthly_transaction_chart(),

            transaction_channel_chart()

        ),

chart_row(

    deposit_withdrawal_chart(),

    daily_transaction_chart()

),

    ]

)
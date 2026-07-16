from dash import Input, Output, html

from components.cards import create_cards
from components.layout import chart_row
from components.charts import (
    monthly_transaction_chart,
    account_type_chart,
    loan_type_chart,
    transaction_channel_chart
)
from components.table import recent_transactions_table
from components.insights import ai_insight_card


def register_dashboard_callbacks(app):

    @app.callback(

        Output("cards-container", "children"),
        Output("dashboard-chart-row-1", "children"),
        Output("dashboard-chart-row-2", "children"),
        Output("recent-transactions-container", "children"),
        Output("dashboard-ai-container", "children"),
        Input("province-filter", "value"),
        Input("account-filter", "value"),
        Input("loan-filter", "value")

    )
    def update_dashboard(
            province,
            account,
            loan
):
        print("Dashboard callback:", province)

        if province is None:
            province = "ALL"

        # KPI Cards
        cards = create_cards(
            province,
            account,
            loan
        )

        # Charts
        row1 = chart_row(
            monthly_transaction_chart(province),
            account_type_chart(province)
        )

        row2 = chart_row(
            loan_type_chart(province),
            transaction_channel_chart(province)
        )

        # Recent Transactions
        table = html.Div(

            [

                html.H3(

                    "Recent Transactions",

                    className="section-title"

                ),

                recent_transactions_table(province)

            ],

            className="table-card"

        )

        # AI Insights
        ai = ai_insight_card(province)

        return (

            cards,

            row1,

            row2,

            table,

            ai

        )
import dash
from dash import html

from components.navbar import create_navbar
from components.cards import create_cards
from components.filters import create_filters
from components.layout import chart_row
from components.table import recent_transactions_table
from components.insights import ai_insight_card

from components.charts import (
    monthly_transaction_chart,
    account_type_chart,
    loan_type_chart,
    transaction_channel_chart,
    top_branches_chart
)

dash.register_page(
    __name__,
    path="/dashboard",
    name="Dashboard"
)

layout = html.Div(

    [

        create_navbar(),

        create_filters(),

        html.Div(

            id="cards-container",

            children=create_cards()

        ),

html.Div(

    id="dashboard-chart-row-1",

    children=chart_row(

        monthly_transaction_chart(),

        account_type_chart()

    )

),

html.Div(

    id="dashboard-chart-row-2",

    children=chart_row(

        loan_type_chart(),

        transaction_channel_chart()

    )

),

html.Div(

    id="recent-transactions-container",

    children=html.Div(

        [

            html.H3(

                "Recent Transactions",

                className="section-title"

            ),

            recent_transactions_table()

        ],

        className="table-card"

    )

),

html.Div(

    id="dashboard-ai-container",

    children=ai_insight_card()

),

        html.Div(

            [

                top_branches_chart()

            ],

            className="chart-card"

        )

    ]

)
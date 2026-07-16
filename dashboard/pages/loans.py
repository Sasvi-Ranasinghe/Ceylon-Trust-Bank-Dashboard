import dash
from dash import html

from utils.data_loader import load_data

from components.layout import chart_row
from components.charts import (
    loan_type_chart,
    loan_status_chart,
    loan_portfolio_chart,
    interest_rate_chart
)
from components.table import top_loans_table
from components.insights import loan_insight_card

from components.table import top_loans_table

from components.insights import loan_insight_card

dash.register_page(
    __name__,
    path="/loans",
    name="Loans"
)

data = load_data()

loans = data["loans"]

approved = len(loans[loans["LoanStatus"] == "Active"])

approval_rate = (approved / len(loans)) * 100

layout = html.Div(

    [

        html.H1(
            "🏦 Loan Analytics",
            className="page-title"
        ),

        html.P(
            "Loan portfolio and credit performance",
            className="page-subtitle"
        ),

        html.Div(

            [

                html.Div(

                    [

                        html.H3("Total Loans"),

                        html.H1(f"{len(loans):,}")

                    ],

                    className="dashboard-card"

                ),

                html.Div(

                    [

                        html.H3("Loan Portfolio"),

                        html.H1(

                            f"LKR {loans['LoanAmount'].sum():,.0f}"

                        )

                    ],

                    className="dashboard-card"

                ),

                html.Div(

                    [

                        html.H3("Active Loans"),

                        html.H1(f"{approved:,}")

                    ],

                    className="dashboard-card"

                ),

                html.Div(

                    [

                        html.H3("Approval Rate"),

                        html.H1(f"{approval_rate:.1f}%")

                    ],

                    className="dashboard-card"

                )

            ],

            className="card-container"

        ),

        chart_row(

            loan_type_chart(),

            loan_status_chart()

        ),

        chart_row(

            loan_portfolio_chart(),

            interest_rate_chart()

        ),

        html.Div(

            [

                html.H3(
                    "Top 10 Highest Loans",
                    className="section-title"
                ),

                top_loans_table()

            ],

            className="table-card"

        ),

        loan_insight_card()

    ]

)
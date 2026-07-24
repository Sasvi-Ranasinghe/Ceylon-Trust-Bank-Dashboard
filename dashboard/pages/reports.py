import dash
from dash import html, dcc

from utils.calculations import *

dash.register_page(
    __name__,
    path="/reports",
    name="Reports"
)

layout = html.Div(

    [

        html.H1(
            "📊 Executive Banking Report",
            className="page-title"
        ),

        html.P(
            "Executive summary of Ceylon Trust Bank PLC",
            className="page-subtitle"
        ),

        # ==========================
        # KPI CARDS
        # ==========================

        html.Div(

            [

                html.Div(
                    [
                        html.H3("Customers"),
                        html.H1(f"{total_customers():,}")
                    ],
                    className="dashboard-card"
                ),

                html.Div(
                    [
                        html.H3("Accounts"),
                        html.H1(f"{total_accounts():,}")
                    ],
                    className="dashboard-card"
                ),

                html.Div(
                    [
                        html.H3("Transactions"),
                        html.H1(f"{total_transactions():,}")
                    ],
                    className="dashboard-card"
                ),

                html.Div(
                    [
                        html.H3("Loans"),
                        html.H1(f"{total_loans():,}")
                    ],
                    className="dashboard-card"
                ),

                html.Div(
                    [
                        html.H3("Deposits"),
                        html.H1(f"LKR {total_deposits():,.0f}")
                    ],
                    className="dashboard-card"
                ),

                html.Div(
                    [
                        html.H3("Loan Portfolio"),
                        html.H1(f"LKR {total_loan_portfolio():,.0f}")
                    ],
                    className="dashboard-card"
                ),

                html.Div(
                    [
                        html.H3("Active Accounts"),
                        html.H1(f"{active_accounts():,}")
                    ],
                    className="dashboard-card"
                ),

                html.Div(
                    [
                        html.H3("Approval Rate"),
                        html.H1(f"{loan_approval_rate()}%")
                    ],
                    className="dashboard-card"
                )

            ],

            className="card-container"

        ),

        # ==========================
        # EXECUTIVE SUMMARY
        # ==========================

        html.Div(

            [

                html.H3(
                    "Executive Summary",
                    className="section-title"
                ),

                html.P(

                    f"""
Ceylon Trust Bank PLC currently manages {total_customers():,} customers across
{total_accounts():,} accounts.

The total deposit portfolio stands at
LKR {total_deposits():,.0f},

while the total loan portfolio has reached
LKR {total_loan_portfolio():,.0f}.

The bank maintains
{active_accounts():,} active accounts

with a loan approval rate of
{loan_approval_rate()}%.
                    """,

                    style={
                        "fontSize": "18px",
                        "lineHeight": "2",
                        "color": "white"
                    }

                )

            ],

            className="table-card"

        ),

        # ==========================
        # EXPORT REPORTS
        # ==========================

        html.Div(

            [

                html.H3(
                    "Export Reports",
                    className="section-title"
                ),

                html.Div(

                    [

                        html.Button(
                            "⬇ Download CSV",
                            id="download-csv-btn",
                            className="download-btn"
                        ),

                        dcc.Download(
                            id="download-csv"
                        ),

                        html.Button(
                            "⬇ Download PDF",
                            id="download-pdf-btn",
                            className="download-btn"
                        ),

                        dcc.Download(
                            id="download-pdf"
                        )

                    ],

                    style={
                        "display": "flex",
                        "gap": "20px"
                    }

                )

            ],

            className="table-card"

        )

    ]

)
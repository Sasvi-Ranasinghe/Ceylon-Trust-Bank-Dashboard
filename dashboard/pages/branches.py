import dash
from dash import html

from utils.data_loader import load_data

from components.layout import chart_row
from components.charts import (
    branch_customer_chart,
    branch_deposit_chart,
    province_branch_chart,
    branch_account_chart
)
from components.table import top_branches_table
from components.insights import branch_insight_card

dash.register_page(
    __name__,
    path="/branches",
    name="Branches"
)

data = load_data()

accounts = data["accounts"]
customers = data["customers"]

total_branches = accounts["BranchName"].nunique()
total_customers = len(customers)
total_deposits = accounts["Balance"].sum()
average_balance = accounts["Balance"].mean()

layout = html.Div(

    [

        html.H1(
            "🏢 Branch Analytics",
            className="page-title"
        ),

        html.P(
            "Branch performance and regional banking analysis",
            className="page-subtitle"
        ),

        html.Div(

            [

                html.Div(
                    [
                        html.H3("Total Branches"),
                        html.H1(f"{total_branches}")
                    ],
                    className="dashboard-card"
                ),

                html.Div(
                    [
                        html.H3("Total Customers"),
                        html.H1(f"{total_customers:,}")
                    ],
                    className="dashboard-card"
                ),

                html.Div(
                    [
                        html.H3("Total Deposits"),
                        html.H1(f"LKR {total_deposits:,.0f}")
                    ],
                    className="dashboard-card"
                ),

                html.Div(
                    [
                        html.H3("Average Balance"),
                        html.H1(f"LKR {average_balance:,.0f}")
                    ],
                    className="dashboard-card"
                )

            ],

            className="card-container"

        ),

        chart_row(

            branch_customer_chart(),

            province_branch_chart()

        ),

        chart_row(

            branch_deposit_chart(),

            branch_account_chart()

        ),

    ]

)
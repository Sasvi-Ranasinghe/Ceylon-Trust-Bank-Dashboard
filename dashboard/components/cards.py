from dash import html
from utils.calculations import *

def create_cards(
    province="ALL",
    account="ALL",
    loan="ALL"
):
    return html.Div(

        [

            create_card(
                "👥",
                "Customers",
                f"{total_customers(province, account, loan):,}"
            ),

            create_card(
                "💳",
                "Accounts",
                f"{total_accounts(province, account, loan):,}"
            ),

            create_card(
                "💸",
                "Transactions",
                f"{total_transactions(province, account, loan):,}"
            ),

            create_card(
                "🏦",
                "Loans",
                f"{total_loans(province, account, loan):,}"
            ),

            create_card(
                "💰",
                "Deposits",
                f"LKR {total_deposits(province, account, loan):,}"
            ),

            create_card(
                "📈",
                "Loan Portfolio",
                f"LKR {total_loan_portfolio(province, account, loan):,}"
            )

        ],

        className="card-container"

    )


def create_card(icon, title, value):

    return html.Div(

        [

            html.Div(icon, className="card-icon"),

            html.P(title, className="card-title"),

            html.H2(value, className="card-value")

        ],

        className="dashboard-card"

    )
from dash import html
import pandas as pd

from utils.data_loader import load_data

data = load_data()

accounts = data["accounts"]
customers = data["customers"]
transactions = data["transactions"]
loans = data["loans"]


def generate_insights(province="ALL"):

    acc = accounts.copy()
    cus = customers.copy()
    trans = transactions.copy()
    loan = loans.copy()

    if province != "ALL":

        customer_ids = cus[
            cus["Province"] == province
        ]["CustomerID"]

        acc = acc[
            acc["CustomerID"].isin(customer_ids)
        ]

        trans = trans[
            trans["CustomerID"].isin(customer_ids)
        ]

        loan = loan[
            loan["CustomerID"].isin(customer_ids)
        ]

    top_account = acc["AccountType"].value_counts().idxmax()

    account_percent = (
        acc["AccountType"]
        .value_counts(normalize=True)
        .max() * 100
    )

    top_channel = trans["Channel"].value_counts().idxmax()

    top_loan = loan["LoanType"].value_counts().idxmax()

    customer_count = len(customer_ids) if province != "ALL" else len(cus)

    return [

        f"{customer_count:,} customers are located in {province if province != 'ALL' else 'all'} Province.",

        f"{top_account} accounts represent {account_percent:.1f}% of accounts.",

        f"{top_channel} is the most frequently used transaction channel.",

        f"{top_loan} is the most common loan category."

    ]

def ai_insight_card(province="ALL"):

    insights = generate_insights(province)

    return html.Div(

        [

            html.H3(

                "🧠 AI Business Insights",

                className="section-title"

            ),

            html.Ul(

                [

                    html.Li(text)

                    for text in insights

                ],

                className="insight-list"

            )

        ],

        className="table-card"

    )

def transaction_insight_card():

    top_channel = (
        transactions["Channel"]
        .value_counts()
        .idxmax()
    )

    total_deposits = (
        transactions[
            transactions["TransactionType"] == "Deposit"
        ]["Amount"].sum()
    )

    total_withdrawals = (
        transactions[
            transactions["TransactionType"] == "Withdrawal"
        ]["Amount"].sum()
    )

    peak_month = (
        pd.to_datetime(
            transactions["TransactionDate"]
        )
        .dt.strftime("%B")
        .value_counts()
        .idxmax()
    )

    return html.Div(

        [

            html.H3(
                "🧠 Transaction Insights",
                className="section-title"
            ),

            html.Ul(

                [

                    html.Li(
                        f"{top_channel} is the most frequently used transaction channel."
                    ),

                    html.Li(
                        f"Total Deposits : LKR {total_deposits:,.0f}"
                    ),

                    html.Li(
                        f"Total Withdrawals : LKR {total_withdrawals:,.0f}"
                    ),

                    html.Li(
                        f"{peak_month} recorded the highest transaction volume."
                    )

                ],

                className="insight-list"

            )

        ],

        className="table-card"

    )

def loan_insight_card():

    top_type = (

        loans["LoanType"]

        .value_counts()

        .idxmax()

    )

    portfolio = loans["LoanAmount"].sum()

    approval_rate = (

        len(

            loans[

                loans["LoanStatus"] == "Active"

            ]

        )

        / len(loans)

    ) * 100

    avg_interest = loans["InterestRate"].mean()

    return html.Div(

        [

            html.H3(

                "🧠 Loan Insights",

                className="section-title"

            ),

            html.Ul(

                [

                    html.Li(

                        f"{top_type} is the most common loan category."

                    ),

                    html.Li(

                        f"Total Loan Portfolio : LKR {portfolio:,.0f}"

                    ),

                    html.Li(

                        f"Active Loan Rate : {approval_rate:.1f}%"

                    ),

                    html.Li(

                        f"Average Interest Rate : {avg_interest:.2f}%"

                    )

                ],

                className="insight-list"

            )

        ],

        className="table-card"

    )

def branch_insight_card():

    deposits = (

        accounts.groupby("BranchName")["Balance"]

        .sum()

    )

    top_branch = deposits.idxmax()

    top_amount = deposits.max()

    busiest_branch = (

        accounts["BranchName"]

        .value_counts()

        .idxmax()

    )

    avg_balance = accounts["Balance"].mean()

    active_accounts = len(

        accounts[
            accounts["Status"] == "Active"
        ]

    )

    return html.Div(

        [

            html.H3(

                "🧠 Branch Insights",

                className="section-title"

            ),

            html.Ul(

                [

                    html.Li(

                        f"{top_branch} Branch has the highest deposits (LKR {top_amount:,.0f})."

                    ),

                    html.Li(

                        f"{busiest_branch} Branch has the highest number of customer accounts."

                    ),

                    html.Li(

                        f"Average account balance across all branches is LKR {avg_balance:,.0f}."

                    ),

                    html.Li(

                        f"{active_accounts:,} accounts are currently Active."

                    )

                ],

                className="insight-list"

            )

        ],

        className="table-card"

    )

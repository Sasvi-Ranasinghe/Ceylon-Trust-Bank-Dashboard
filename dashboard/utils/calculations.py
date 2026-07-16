from utils.data_loader import load_data

data = load_data()


customers = data["customers"]

accounts = data["accounts"]

transactions = data["transactions"]

loans = data["loans"]

from utils.filters import filter_data

def total_customers(
    province="ALL",
    account="ALL",
    loan="ALL"
):
    return len(
        filter_data(
            province,
            account,
            loan
        )["customers"]
    )

def total_accounts(
    province="ALL",
    account="ALL",
    loan="ALL"
):

    return len(
        filter_data(
            province,
            account,
            loan
        )["accounts"]
    )


def total_transactions(
    province="ALL",
    account="ALL",
    loan="ALL"
):

    return len(
        filter_data(
            province,
            account,
            loan
        )["transactions"]
    )


def total_loans(
    province="ALL",
    account="ALL",
    loan="ALL"
):

    return len(
        filter_data(
            province,
            account,
            loan
        )["loans"]
    )


def total_deposits(
    province="ALL",
    account="ALL",
    loan="ALL"
):

    return (
        filter_data(
            province,
            account,
            loan
        )["accounts"]["Balance"].sum()
    )

def total_loan_portfolio(
    province="ALL",
    account="ALL",
    loan="ALL"
):

    return (
        filter_data(
            province,
            account,
            loan
        )["loans"]["LoanAmount"].sum()
    )

# ==========================================
# EXECUTIVE SUMMARY CALCULATIONS
# ==========================================

def today_deposits():

    return transactions[
        transactions["TransactionType"] == "Deposit"
    ]["Amount"].sum()


def today_withdrawals():

    return transactions[
        transactions["TransactionType"] == "Withdrawal"
    ]["Amount"].sum()


def active_accounts():

    return len(
        accounts[
            accounts["Status"] == "Active"
        ]
    )


def loan_approval_rate():

    approved = len(
        loans[
            loans["LoanStatus"] == "Approved"
        ]
    )

    total = len(loans)

    if total == 0:
        return 0

    return round((approved / total) * 100, 1)
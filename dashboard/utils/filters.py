from utils.data_loader import load_data

data = load_data()

customers = data["customers"]
accounts = data["accounts"]
transactions = data["transactions"]
loans = data["loans"]


def filter_data(
    province="ALL",
    account="ALL",
    loan="ALL"
):
    cus = customers.copy()
    acc = accounts.copy()
    trans = transactions.copy()
    loan_df = loans.copy()

    # Province Filter
    if province != "ALL":

        cus = cus[
            cus["Province"] == province
        ]

    customer_ids = cus["CustomerID"]

    acc = acc[
        acc["CustomerID"].isin(customer_ids)
    ]

    # Account Filter
    if account != "ALL":

        acc = acc[
            acc["AccountType"] == account
        ]

    account_numbers = acc["AccountNo"]

    trans = trans[
        trans["AccountNo"].isin(account_numbers)
    ]

    loan_df = loan_df[
        loan_df["CustomerID"].isin(customer_ids)
    ]

    # Loan Filter
    if loan != "ALL":

        loan_df = loan_df[
            loan_df["LoanType"] == loan
        ]

    return {
        "customers": cus,
        "accounts": acc,
        "transactions": trans,
        "loans": loan_df
    }
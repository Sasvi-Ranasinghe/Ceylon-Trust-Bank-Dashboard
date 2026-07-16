import pandas as pd


def load_data():

    customers = pd.read_csv("../data/customers.csv")

    accounts = pd.read_csv("../data/accounts.csv")

    transactions = pd.read_csv("../data/transactions.csv")

    loans = pd.read_csv("../data/loans.csv")

    return {

        "customers": customers,

        "accounts": accounts,

        "transactions": transactions,

        "loans": loans

    }
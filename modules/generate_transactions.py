import random
import pandas as pd
from datetime import datetime, timedelta

# =====================================================
# LOAD DATA
# =====================================================

accounts = pd.read_csv("../data/accounts.csv")
customers = pd.read_csv("../data/customers.csv")

transactions = []

# =====================================================
# SETTINGS
# =====================================================

NUMBER_OF_TRANSACTIONS = 10000

TRANSACTION_TYPES = {
    "Deposit": 30,
    "Withdrawal": 25,
    "Transfer": 20,
    "Bill Payment": 10,
    "Online Purchase": 8,
    "Salary Credit": 5,
    "Interest Credit": 2
}

CHANNELS = {
    "ATM": 20,
    "Branch": 15,
    "Mobile Banking": 30,
    "Internet Banking": 20,
    "CDM": 10,
    "POS": 5
}

STATUS = {
    "Successful": 97,
    "Failed": 2,
    "Pending": 1
}

# =====================================================
# AMOUNT RULES
# =====================================================

AMOUNT_RULES = {

    "Deposit": (1000,100000),

    "Withdrawal": (500,50000),

    "Transfer": (500,200000),

    "Bill Payment": (500,50000),

    "Online Purchase": (200,75000),

    "Salary Credit": (30000,500000),

    "Interest Credit": (100,15000)

}

# =====================================================
# HELPER FUNCTIONS
# =====================================================

def choose_transaction_type():

    return random.choices(

        list(TRANSACTION_TYPES.keys()),

        weights=list(TRANSACTION_TYPES.values()),

        k=1

    )[0]


def choose_channel():

    return random.choices(

        list(CHANNELS.keys()),

        weights=list(CHANNELS.values()),

        k=1

    )[0]


def choose_status():

    return random.choices(

        list(STATUS.keys()),

        weights=list(STATUS.values()),

        k=1

    )[0]

def generate_amount(transaction_type):

    minimum, maximum = AMOUNT_RULES[transaction_type]

    return random.randint(minimum, maximum)

print("✅ Configuration Loaded")

# ======================================
# Transaction Date
# ======================================

def generate_transaction_date(open_date):

    open_date = datetime.strptime(open_date, "%Y-%m-%d")

    today = datetime.today()

    days = (today - open_date).days


    if days <= 0:
        return open_date.strftime("%Y-%m-%d")

    random_days = random.randint(0, days)

    transaction_date = open_date + timedelta(days=random_days)

    return transaction_date.strftime("%Y-%m-%d")
# =====================================================
# DESCRIPTION
# =====================================================

def generate_description(transaction_type):

    descriptions = {

        "Deposit": [
            "Cash Deposit",
            "CDM Deposit",
            "Cheque Deposit"
        ],

        "Withdrawal": [
            "ATM Withdrawal",
            "Cash Withdrawal",
            "Branch Withdrawal"
        ],

        "Transfer": [
            "Fund Transfer",
            "Online Transfer",
            "Bank Transfer"
        ],

        "Bill Payment": [
            "CEB Bill",
            "Water Bill",
            "Dialog Bill",
            "Mobitel Bill"
        ],

        "Online Purchase": [
            "Daraz Purchase",
            "Uber Payment",
            "Keells Online",
            "Amazon Purchase"
        ],

        "Salary Credit": [
            "Monthly Salary"
        ],

        "Interest Credit": [
            "Interest Credit"
        ]

    }

    return random.choice(descriptions[transaction_type])


# =====================================================
# BALANCE AFTER TRANSACTION
# =====================================================

def calculate_balance(balance, transaction_type, amount):

    if transaction_type in ["Deposit", "Salary Credit", "Interest Credit"]:

        balance += amount

    else:

        balance -= amount

        if balance < 0:
            balance = 0

    return balance


# =====================================================
# TRANSACTION GENERATOR
# =====================================================

def generate_transaction(account, transaction_number, current_balance):

    transaction_type = choose_transaction_type()

    amount = generate_amount(transaction_type)

    balance_after = calculate_balance(
        current_balance,
        transaction_type,
        amount
    )

    current_balance = balance_after

    transaction = {

        "TransactionID": f"TRX{transaction_number:07d}",

        "AccountNo": account["AccountNo"],

        "CustomerID": account["CustomerID"],

        "TransactionDate":
            generate_transaction_date(account["OpenDate"]),

        "TransactionType": transaction_type,

        "Channel": choose_channel(),

        "Amount": amount,

        "BalanceAfter": balance_after,

        "Description":
            generate_description(transaction_type),

        "Status": choose_status()

    }

    return transaction

# =====================================================
# MAIN PROGRAM
# =====================================================

transaction_number = 1

for _, account in accounts.iterrows():

    current_balance = account["Balance"]

    number_of_transactions = random.randint(15, 25)

    for _ in range(number_of_transactions):

        transaction = generate_transaction(

            account,

            transaction_number,

            current_balance

        )

        current_balance = transaction["BalanceAfter"]

        transactions.append(transaction)

        transaction_number += 1

# =====================================================
# CREATE DATAFRAME
# =====================================================

transactions_df = pd.DataFrame(transactions)

# =====================================================
# SORT BY DATE
# =====================================================

transactions_df = transactions_df.sort_values(
    by="TransactionDate"
)

# =====================================================
# EXPORT CSV
# =====================================================

transactions_df.to_csv(
    "../data/transactions.csv",
    index=False
)

# =====================================================
# SUMMARY
# =====================================================

print("\n" + "=" * 60)
print("      BankInsight Transaction Generator")
print("=" * 60)

print(f"Accounts Loaded       : {len(accounts)}")
print(f"Transactions Created  : {len(transactions_df)}")

print("\nTransaction Types")

print(transactions_df["TransactionType"].value_counts())

print("\nTransaction Status")

print(transactions_df["Status"].value_counts())

print("\nTotal Transaction Value")

print(f"LKR {transactions_df['Amount'].sum():,.2f}")

print("\nCSV Saved Successfully")

print("Location : data/transactions.csv")

print("=" * 60)



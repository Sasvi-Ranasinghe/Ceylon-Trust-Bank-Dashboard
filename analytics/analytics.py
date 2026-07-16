import pandas as pd

# =====================================================
# LOAD DATA
# =====================================================

customers = pd.read_csv("../data/customers.csv")
accounts = pd.read_csv("../data/accounts.csv")
transactions = pd.read_csv("../data/transactions.csv")
loans = pd.read_csv("../data/loans.csv")

print("=" * 60)
print("              BankInsight Analytics")
print("=" * 60)
print("Data Loaded Successfully\n")


# =====================================================
# CUSTOMER SUMMARY
# =====================================================

def customer_summary():

    print("=" * 60)
    print("CUSTOMER SUMMARY")
    print("=" * 60)

    print(f"Total Customers : {len(customers)}")

    print("\nGender Distribution")
    print(customers["Gender"].value_counts())

    print("\nProvince Distribution")
    print(customers["Province"].value_counts())

    print("\nTop 10 Occupations")
    print(customers["Occupation"].value_counts().head(10))

    print()


# =====================================================
# ACCOUNT SUMMARY
# =====================================================

def account_summary():

    print("=" * 60)
    print("ACCOUNT SUMMARY")
    print("=" * 60)

    print(f"Total Accounts : {len(accounts)}")

    print("\nAccount Types")
    print(accounts["AccountType"].value_counts())

    print("\nAccount Status")
    print(accounts["Status"].value_counts())

    print("\nTotal Deposits")
    print(f"LKR {accounts['Balance'].sum():,.2f}")

    print("\nAverage Balance")
    print(f"LKR {accounts['Balance'].mean():,.2f}")

    print()


# =====================================================
# TRANSACTION SUMMARY
# =====================================================

def transaction_summary():

    print("=" * 60)
    print("TRANSACTION SUMMARY")
    print("=" * 60)

    print(f"Total Transactions : {len(transactions)}")

    print("\nTransaction Types")
    print(transactions["TransactionType"].value_counts())

    print("\nTransaction Status")
    print(transactions["Status"].value_counts())

    print("\nTransaction Channels")
    print(transactions["Channel"].value_counts())

    print("\nTotal Transaction Value")
    print(f"LKR {transactions['Amount'].sum():,.2f}")

    print()


# =====================================================
# LOAN SUMMARY
# =====================================================

def loan_summary():

    print("=" * 60)
    print("LOAN SUMMARY")
    print("=" * 60)

    print(f"Total Loans : {len(loans)}")

    print("\nLoan Types")
    print(loans["LoanType"].value_counts())

    print("\nLoan Status")
    print(loans["LoanStatus"].value_counts())

    print("\nTotal Loan Portfolio")
    print(f"LKR {loans['LoanAmount'].sum():,.2f}")

    print("\nAverage Monthly EMI")
    print(f"LKR {loans['MonthlyInstallment'].mean():,.2f}")

    print()


# =====================================================
# EXECUTIVE SUMMARY
# =====================================================

def executive_summary():

    print("=" * 60)
    print("EXECUTIVE DASHBOARD")
    print("=" * 60)

    print(f"Customers        : {len(customers)}")
    print(f"Accounts         : {len(accounts)}")
    print(f"Transactions     : {len(transactions)}")
    print(f"Loans            : {len(loans)}")

    print()

    print(f"Total Deposits   : LKR {accounts['Balance'].sum():,.2f}")
    print(f"Loan Portfolio   : LKR {loans['LoanAmount'].sum():,.2f}")
    print(f"Transaction Value: LKR {transactions['Amount'].sum():,.2f}")

    print()


# =====================================================
# MAIN
# =====================================================

def main():

    customer_summary()

    account_summary()

    transaction_summary()

    loan_summary()

    executive_summary()


if __name__ == "__main__":
    main()
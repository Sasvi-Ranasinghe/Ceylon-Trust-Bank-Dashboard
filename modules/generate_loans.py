import random
import pandas as pd
from datetime import datetime, timedelta

# =====================================================
# LOAD DATA
# =====================================================

customers = pd.read_csv("../data/customers.csv")
accounts = pd.read_csv("../data/accounts.csv")

loans = []

# =====================================================
# SETTINGS
# =====================================================

NUMBER_OF_LOANS = 150

LOAN_TYPES = {
    "Personal Loan": 35,
    "Home Loan": 25,
    "Vehicle Loan": 20,
    "Business Loan": 15,
    "Education Loan": 5
}

LOAN_STATUS = {
    "Active": 85,
    "Completed": 10,
    "Defaulted": 5
}

# =====================================================
# INTEREST RATES
# =====================================================

INTEREST_RATES = {
    "Personal Loan": 14.5,
    "Home Loan": 9.5,
    "Vehicle Loan": 11.5,
    "Business Loan": 13.5,
    "Education Loan": 8.5
}

# =====================================================
# LOAN AMOUNT RANGE
# =====================================================

AMOUNT_RANGE = {

    "Personal Loan": (100000, 2000000),

    "Home Loan": (2000000, 25000000),

    "Vehicle Loan": (500000, 8000000),

    "Business Loan": (500000, 15000000),

    "Education Loan": (200000, 5000000)

}

# =====================================================
# LOAN TERM (YEARS)
# =====================================================

TERM_RANGE = {

    "Personal Loan": (1, 5),

    "Home Loan": (10, 30),

    "Vehicle Loan": (3, 7),

    "Business Loan": (2, 10),

    "Education Loan": (2, 8)

}

# =====================================================
# HELPER FUNCTIONS
# =====================================================

def choose_loan_type():

    return random.choices(

        list(LOAN_TYPES.keys()),

        weights=list(LOAN_TYPES.values()),

        k=1

    )[0]


def choose_status():

    return random.choices(

        list(LOAN_STATUS.keys()),

        weights=list(LOAN_STATUS.values()),

        k=1

    )[0]


def generate_amount(loan_type):

    minimum, maximum = AMOUNT_RANGE[loan_type]

    return random.randint(minimum, maximum)


def generate_term(loan_type):

    minimum, maximum = TERM_RANGE[loan_type]

    return random.randint(minimum, maximum)

print("✅ Loan Configuration Loaded")

# =====================================================
# EMI CALCULATOR
# =====================================================

def calculate_emi(principal, annual_rate, years):

    monthly_rate = annual_rate / 100 / 12

    months = years * 12

    if monthly_rate == 0:
        return round(principal / months, 2)

    emi = (
        principal
        * monthly_rate
        * (1 + monthly_rate) ** months
    ) / (
        (1 + monthly_rate) ** months - 1
    )

    return round(emi, 2)


# =====================================================
# LOAN DATES
# =====================================================

def generate_loan_dates(join_date, years):

    join_date = datetime.strptime(join_date, "%Y-%m-%d")

    today = datetime.today()

    total_days = (today - join_date).days

    if total_days <= 0:
        start_date = join_date

    else:
        start_date = join_date + timedelta(
            days=random.randint(0, total_days)
        )

    end_date = start_date + timedelta(days=years * 365)

    return (
        start_date.strftime("%Y-%m-%d"),
        end_date.strftime("%Y-%m-%d")
    )


# =====================================================
# LOAN ELIGIBILITY
# =====================================================

def eligible_for_loan(account):

    return (
        account["Status"] == "Active"
        and account["Balance"] >= 50000
    )


# =====================================================
# LOAN GENERATOR
# =====================================================

def generate_loan(customer, account, loan_number):

    loan_type = choose_loan_type()

    amount = generate_amount(loan_type)

    years = generate_term(loan_type)

    interest = INTEREST_RATES[loan_type]

    emi = calculate_emi(
        amount,
        interest,
        years
    )

    start_date, end_date = generate_loan_dates(
        customer["JoinDate"],
        years
    )

    loan = {

        "LoanID": f"LN{loan_number:05d}",

        "CustomerID": customer["CustomerID"],

        "AccountNo": account["AccountNo"],

        "LoanType": loan_type,

        "LoanAmount": amount,

        "InterestRate": interest,

        "LoanTermYears": years,

        "MonthlyInstallment": emi,

        "StartDate": start_date,

        "EndDate": end_date,

        "LoanStatus": choose_status()

    }

    return loan

# =====================================================
# MAIN PROGRAM
# =====================================================

loan_number = 1

# CustomerID -> Account mapping
account_lookup = {}

for _, account in accounts.iterrows():
    account_lookup[account["CustomerID"]] = account

# Keep track of customers who already received a loan
customers_with_loans = set()

# Shuffle customers for randomness
customers_shuffled = customers.sample(frac=1).reset_index(drop=True)

for _, customer in customers_shuffled.iterrows():

    if loan_number > NUMBER_OF_LOANS:
        break

    customer_id = customer["CustomerID"]

    # Skip if customer has no account
    if customer_id not in account_lookup:
        continue

    account = account_lookup[customer_id]

    # Skip if customer already has a loan
    if customer_id in customers_with_loans:
        continue

    # Check loan eligibility
    if not eligible_for_loan(account):
        continue

    loan = generate_loan(
        customer,
        account,
        loan_number
    )

    loans.append(loan)

    customers_with_loans.add(customer_id)

    loan_number += 1

# =====================================================
# CREATE DATAFRAME
# =====================================================

loans_df = pd.DataFrame(loans)

# =====================================================
# EXPORT CSV
# =====================================================

loans_df.to_csv(
    "../data/loans.csv",
    index=False
)

# =====================================================
# SUMMARY
# =====================================================

print("\n" + "=" * 60)
print("          BankInsight Loan Generator")
print("=" * 60)

print(f"Customers Loaded : {len(customers)}")
print(f"Loans Created    : {len(loans_df)}")

print("\nLoan Type Summary")
print(loans_df["LoanType"].value_counts())

print("\nLoan Status Summary")
print(loans_df["LoanStatus"].value_counts())

print("\nTotal Loan Portfolio")
print(f"LKR {loans_df['LoanAmount'].sum():,.2f}")

print("\nAverage Monthly EMI")
print(f"LKR {loans_df['MonthlyInstallment'].mean():,.2f}")

print("\nCSV File Saved Successfully")
print("Location : data/loans.csv")

print("=" * 60)

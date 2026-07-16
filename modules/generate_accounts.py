import random
import pandas as pd
from datetime import datetime, timedelta

# =====================================================
# LOAD DATA
# =====================================================

customers = pd.read_csv("../data/customers.csv")
branches = pd.read_csv("../data/branches.csv")

accounts = []

# =====================================================
# ACCOUNT SETTINGS
# =====================================================

ACCOUNT_DISTRIBUTION = {
    "Savings": 70,
    "Current": 20,
    "Fixed Deposit": 10
}

STATUS_DISTRIBUTION = {
    "Active": 90,
    "Dormant": 8,
    "Closed": 2
}

INTEREST_RATES = {
    "Savings": 2.5,
    "Current": 0.0,
    "Fixed Deposit": 8.5
}

CURRENCY = "LKR"

# =====================================================
# HELPER FUNCTIONS
# =====================================================

def choose_account_type():
    return random.choices(
        list(ACCOUNT_DISTRIBUTION.keys()),
        weights=list(ACCOUNT_DISTRIBUTION.values()),
        k=1
    )[0]


def choose_status():
    return random.choices(
        list(STATUS_DISTRIBUTION.keys()),
        weights=list(STATUS_DISTRIBUTION.values()),
        k=1
    )[0]


def generate_balance(account_type):

    if account_type == "Savings":
        return random.randint(10000, 500000)

    elif account_type == "Current":
        return random.randint(25000, 2000000)

    elif account_type == "Fixed Deposit":
        return random.randint(100000, 5000000)


def atm_card(account_type):

    if account_type == "Fixed Deposit":
        return "No"

    return "Yes"


def internet_banking():

    return random.choices(
        ["Enabled", "Disabled"],
        weights=[85,15],
        k=1
    )[0]


def mobile_banking():

    return random.choices(
        ["Enabled","Disabled"],
        weights=[90,10],
        k=1
    )[0]


def kyc_status():

    return random.choices(
        ["Verified","Pending"],
        weights=[97,3],
        k=1
    )[0]


def risk_level(balance):

    if balance >= 1000000:
        return "High"

    elif balance >= 250000:
        return "Medium"

    return "Low"

# =====================================================
# BRANCH MAPPING
# =====================================================

province_branches = {}

for _, branch in branches.iterrows():

    province = branch["Province"]

    if province not in province_branches:
        province_branches[province] = []

    province_branches[province].append(branch)

print("✅ Configuration Loaded")

# =====================================================
# OPEN DATE GENERATOR
# =====================================================

def generate_open_date(join_date):

    join_date = datetime.strptime(join_date, "%Y-%m-%d")

    today = datetime.today()

    total_days = (today - join_date).days

    if total_days <= 0:
        return join_date.strftime("%Y-%m-%d")

    random_days = random.randint(0, total_days)

    open_date = join_date + timedelta(days=random_days)

    return open_date.strftime("%Y-%m-%d")


# =====================================================
# ACCOUNT GENERATOR
# =====================================================

def generate_account(customer, account_number):

    account_type = choose_account_type()

    province = customer["Province"]

    available_branches = province_branches[province]

    selected_branch = random.choice(available_branches)

    branch_id = selected_branch["BranchID"]

    branch_name = selected_branch["BranchName"]

    balance = generate_balance(account_type)

    account = {

        "AccountNo": f"ACC{account_number:06d}",

        "CustomerID": customer["CustomerID"],

        "AccountType": account_type,

        "BranchID": branch_id,

        "BranchName": branch_name,

        "Currency": CURRENCY,

        "Balance": balance,

        "InterestRate": INTEREST_RATES[account_type],

        "Status": choose_status(),

        "ATMCard": atm_card(account_type),

        "InternetBanking": internet_banking(),

        "MobileBanking": mobile_banking(),

        "KYCStatus": kyc_status(),

        "RiskLevel": risk_level(balance),

        "OpenDate": generate_open_date(customer["JoinDate"])

    }

    return account

# =====================================================
# MAIN PROGRAM
# =====================================================

account_number = 1

for _, customer in customers.iterrows():

    account = generate_account(customer, account_number)

    accounts.append(account)

    account_number += 1

# =====================================================
# CREATE DATAFRAME
# =====================================================

accounts_df = pd.DataFrame(accounts)

# =====================================================
# EXPORT CSV
# =====================================================

accounts_df.to_csv("../data/accounts.csv", index=False)

# =====================================================
# SUMMARY
# =====================================================

print("\n" + "=" * 60)
print("         BankInsight Account Generator")
print("=" * 60)

print(f"Total Customers : {len(customers)}")
print(f"Accounts Created: {len(accounts_df)}")

print("\nAccount Type Summary")

print(accounts_df["AccountType"].value_counts())

print("\nAccount Status Summary")

print(accounts_df["Status"].value_counts())

print("\nAverage Balance by Account Type")

print(
    accounts_df.groupby("AccountType")["Balance"]
    .mean()
    .round(2)
)

print("\nCSV File Saved Successfully")

print("Location : data/accounts.csv")

print("=" * 60)

import random
import pandas as pd
from datetime import datetime, timedelta

# ----------------------------------------
# Name Lists
# ----------------------------------------

male_names = [
    "Kasun","Nimal","Amal","Chathura","Lakshan",
    "Tharindu","Diniru","Anjan","Praveen","Akil",
    "Hashan","Yugantha","Miyuru","Shevon","Aravinda",
    "Isuru","Kavindu","Pasindu","Chamara","Supun"
]

female_names = [
    "Nadeesha","Tharushi","Sanduni","Dilani","Ishara",
    "Eshani","Ranuji","Ramudi","Piumandi","Taniya",
    "Dinethma","Roshani","Karlina","Seelawathi",
    "Karunawathi","Sachini","Hiruni","Yashoda",
    "Imesha","Vihangi"
]

last_names = [
    "Perera","Silva","Fernando","Jayasinghe",
    "Ranasinghe","Gunawardena","Wijesinghe",
    "Karunaratne","Senanayake","Abeysekera",
    "Rajapaksha","Dissanayake","Bandara",
    "Ekanayake","Wickramasinghe","Herath",
    "Weerasinghe","Fonseka","Pathirana","Madushan"
]

# ----------------------------------------
# Sri Lankan Locations
# ----------------------------------------

province_city = {

    "Western": [
        "Colombo",
        "Gampaha",
        "Kalutara"
    ],

    "Central": [
        "Kandy",
        "Matale",
        "Nuwara Eliya"
    ],

    "Southern": [
        "Galle",
        "Matara",
        "Hambantota"
    ],

    "Northern": [
        "Jaffna",
        "Kilinochchi",
        "Vavuniya"
    ],

    "Eastern": [
        "Batticaloa",
        "Trincomalee",
        "Ampara"
    ],

    "North Western": [
        "Kurunegala",
        "Puttalam"
    ],

    "North Central": [
        "Anuradhapura",
        "Polonnaruwa"
    ],

    "Uva": [
        "Badulla",
        "Monaragala"
    ],

    "Sabaragamuwa": [
        "Ratnapura",
        "Kegalle"
    ]
}

# ----------------------------------------
# Occupation & Income
# ----------------------------------------

occupations = {

    "Software Engineer": (180000,350000),

    "Bank Officer": (90000,180000),

    "Teacher": (65000,130000),

    "Doctor": (250000,500000),

    "Accountant": (90000,220000),

    "Business Owner": (150000,600000),

    "Manager": (180000,400000),

    "Engineer": (150000,300000),

    "Lawyer": (180000,450000),

    "Nurse": (70000,140000),

    "Government Officer": (70000,150000),

    "Student": (0,0),

    "Sales Executive": (60000,120000),

    "Marketing Executive": (70000,160000),

    "Data Analyst": (150000,280000)
}

# ----------------------------------------
# Mobile Prefixes
# ----------------------------------------

mobile_prefixes = [
    "070",
    "071",
    "072",
    "074",
    "075",
    "076",
    "077",
    "078"
]

# ----------------------------------------
# Email Domains
# ----------------------------------------

email_domains = [
    "gmail.com",
    "outlook.com",
    "yahoo.com"
]

# ----------------------------------------
# Date Settings
# ----------------------------------------

dob_start = datetime(1960,1,1)
dob_end = datetime(2005,12,31)

today = datetime.today()

# ----------------------------------------
# Helper Functions
# ----------------------------------------

def generate_nic(dob):
    year = dob.year % 100
    day = dob.timetuple().tm_yday

    if day > 500:
        day = 500

    serial = random.randint(1000, 9999)

    return f"{year:02d}{day:03d}{serial}V"


def generate_mobile():
    prefix = random.choice(mobile_prefixes)
    number = random.randint(1000000, 9999999)
    return f"{prefix}{number}"


def generate_email(first_name, last_name):
    domain = random.choice(email_domains)
    number = random.randint(1, 999)
    return f"{first_name.lower()}.{last_name.lower()}{number}@{domain}"


def generate_join_date(dob):

    minimum_join_age = 18

    try:
        join_start = dob.replace(year=dob.year + minimum_join_age)

    except ValueError:
        # Handle February 29 -> February 28
        join_start = dob.replace(
            year=dob.year + minimum_join_age,
            day=28
        )

    if join_start > today:
        join_start = today

    days = (today - join_start).days

    if days <= 0:
        return today.strftime("%Y-%m-%d")

    random_days = random.randint(0, days)

    join_date = join_start + timedelta(days=random_days)

    return join_date.strftime("%Y-%m-%d")

def generate_dob():

    age_group = random.choices(

        ["18-25", "26-40", "41-60", "61-65"],

        weights=[20, 40, 30, 10],

        k=1

    )[0]

    current_year = today.year

    if age_group == "18-25":
        year = random.randint(current_year - 25, current_year - 18)

    elif age_group == "26-40":
        year = random.randint(current_year - 40, current_year - 26)

    elif age_group == "41-60":
        year = random.randint(current_year - 60, current_year - 41)

    else:
        year = random.randint(current_year - 65, current_year - 61)

    month = random.randint(1, 12)

    day = random.randint(1, 28)

    return datetime(year, month, day)

def generate_customer(customer_id):
    gender = random.choices(
        ["Male", "Female"],
        weights=[55, 45],
        k=1
    )[0]

    if gender == "Male":
        first_name = random.choice(male_names)
    else:
        first_name = random.choice(female_names)

    last_name = random.choice(last_names)

    province = random.choices(

        list(province_city.keys()),

        weights=[
            32,  # Western
            13,  # Central
            12,  # Southern
            5,  # Northern
            8,  # Eastern
            12,  # North Western
            6,  # North Central
            5,  # Uva
            7  # Sabaragamuwa
        ],

        k=1

    )[0]
    city = random.choice(province_city[province])

    dob = generate_dob()

    age = today.year - dob.year

    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1
    occupation = random.choices(

        list(occupations.keys()),

        weights=[

            6,  # Software Engineer
            12,  # Bank Officer
            12,  # Teacher
            4,  # Doctor
            8,  # Accountant
            10,  # Business Owner
            10,  # Manager
            8,  # Engineer
            3,  # Lawyer
            8,  # Nurse
            14,  # Government Officer
            5,  # Student
            10,  # Sales Executive
            6,  # Marketing Executive
            6  # Data Analyst

        ],

        k=1

    )[0]

    income_range = occupations[occupation]

    if income_range[0] == income_range[1]:
        monthly_income = income_range[0]
    else:
        monthly_income = random.randint(income_range[0], income_range[1])

    customer = {

        "CustomerID": customer_id,

        "FirstName": first_name,

        "LastName": last_name,

        "Gender": gender,

        "DOB": dob.strftime("%Y-%m-%d"),

        "Age": age,

        "NIC": generate_nic(dob),

        "Mobile": generate_mobile(),

        "Email": generate_email(first_name, last_name),

        "Province": province,

        "City": city,

        "Occupation": occupation,

        "MonthlyIncome": monthly_income,

        "JoinDate": generate_join_date(dob)

    }

    return customer
# ----------------------------------------
# Main Program
# ----------------------------------------

customers = []

NUMBER_OF_CUSTOMERS = 500

for i in range(1, NUMBER_OF_CUSTOMERS + 1):

    customer_id = f"C{i:04d}"

    customer = generate_customer(customer_id)

    customers.append(customer)

# ----------------------------------------
# Create DataFrame
# ----------------------------------------

df = pd.DataFrame(customers)

# ----------------------------------------
# Save CSV
# ----------------------------------------

df.to_csv("../data/customers.csv", index=False)

print("=" * 50)
print(" BankInsight Customer Generator")
print("=" * 50)
print(f"Customers Generated : {len(df)}")
print("Output File         : customers.csv")
print("=" * 50)
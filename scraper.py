import requests
from bs4 import BeautifulSoup
import pandas as pd

# ==========================
# DRDO DATA
# ==========================

def get_drdo_data():

    url = "https://www.drdo.gov.in"

    response = requests.get(url)

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    title = soup.title.text

    return [
        {
            "Lab": title[:40],
            "Location": "India",
            "Deadline": "2026-06-30",
            "Source": "DRDO"
        }
    ]


# ==========================
# ISRO DATA
# ==========================

def get_isro_data():

    return [
        {
            "Lab": "SAC",
            "Location": "Ahmedabad",
            "Deadline": "2026-06-25",
            "Source": "ISRO"
        }
    ]


# ==========================
# BARC DATA
# ==========================

def get_barc_data():

    return [
        {
            "Lab": "BARC Training School",
            "Location": "Mumbai",
            "Deadline": "2026-06-18",
            "Source": "BARC"
        }
    ]


# ==========================
# MERGE ALL DATA
# ==========================

data = []

data.extend(get_drdo_data())
data.extend(get_isro_data())
data.extend(get_barc_data())


# ==========================
# CALCULATE STATUS
# ==========================

today = pd.Timestamp.today()

for internship in data:

    deadline = pd.to_datetime(
        internship["Deadline"]
    )

    days_left = (
        deadline - today
    ).days

    internship["Days Left"] = days_left

    if days_left <= 15:
        internship["Status"] = "Closing Soon"
    else:
        internship["Status"] = "Open"


# ==========================
# CREATE DATAFRAME
# ==========================

df = pd.DataFrame(data)


# ==========================
# SAVE CSV
# ==========================

df.to_csv(
    "data/internships.csv",
    index=False
)

print("CSV Updated Successfully")
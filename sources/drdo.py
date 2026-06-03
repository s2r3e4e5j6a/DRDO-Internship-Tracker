import requests
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup

def get_drdo_data():

    url = "https://www.drdo.gov.in/drdo/offerings/vacancies"

    response = requests.get(url)

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    tables = soup.find_all("table")

    print("Tables found:", len(tables))

    return [
        {
            "Lab": "DRDO Test",
            "Location": "India",
            "Deadline": "2026-06-30",
            "Source": "DRDO"
        }
    ]
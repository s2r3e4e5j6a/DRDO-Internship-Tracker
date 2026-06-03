import requests
from bs4 import BeautifulSoup


def get_start_data():

    url = "https://www.isro.gov.in/START2026.html"

    response = requests.get(url)

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    return [
        {
            "Lab": "START 2026",
            "Location": "Online",
            "Deadline": "2026-02-13",
            "Source": "ISRO",
            "Status": "Open"
        }
    ]


if __name__ == "__main__":

    print(get_start_data())
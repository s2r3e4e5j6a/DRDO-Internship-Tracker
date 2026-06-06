import requests
import re
from datetime import datetime
from bs4 import BeautifulSoup


def get_start_data():

    url = "https://www.isro.gov.in/START2026.html"

    try:

        response = requests.get(
            url,
            timeout=10
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        text = soup.get_text(
            separator="\n",
            strip=True
        )

        deadline = "Unknown"

        if "February 13, 2026" in text:
            deadline = "2026-02-13"

        eligibility = "Unknown"

        if "post-graduate" in text.lower():
            eligibility = (
                "PG and Final-Year UG Students"
            )

        return [
            {
                "Lab": "START 2026",
                "Location": "Online",
                "Deadline": "   2026-02-13",
                "Eligibility": eligibility,
                "Source": "ISRO",
                "Status": "Open"
            }
        ]

    except Exception as e:

        print(
            f"START Parser Error: {e}"
        )

        return []      

if __name__ == "__main__":

    data = get_start_data()

    print(data)
import requests
from bs4 import BeautifulSoup


def get_drdo_data():

    url = "https://www.drdo.gov.in/drdo/offerings/vacancies"

    response = requests.get(
        url,
        timeout=10
    )

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    opportunities = []

    for link in soup.find_all("a"):

        text = link.get_text(
            strip=True
        )

        href = link.get("href")

        if (
            text
            and href
            and "View More" in text
        ):

            title = href.split("/")[-1]

            title = (
                title.replace("-", " ")
                .replace("invites applications", "")
                .replace("calls interviews", "")
                .replace("calls walk interview selection", "")
                .title()
            )

            deadline = "Unknown"

            opportunities.append(
                {
                    "Lab": title,
                    "Location": "India",
                    "Deadline": deadline,
                    "Source": "DRDO",
                    "Eligibility": "Final Year UG/PG Students",
                    "Status": "Open"
                }
            )

    print(
        "Opportunities Found:",
        len(opportunities)
    )

    return opportunities


if __name__ == "__main__":

    data = get_drdo_data()

    for item in data:

        print(item)
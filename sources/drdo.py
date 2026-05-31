import requests
from bs4 import BeautifulSoup

url = "https://www.drdo.gov.in/drdo/offerings/vacancies"

response = requests.get(url)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

for heading in soup.find_all(["h1", "h2", "h3", "h4"]):

    text = heading.get_text(strip=True)

    if text:
        print(text)
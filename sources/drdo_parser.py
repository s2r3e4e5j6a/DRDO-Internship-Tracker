import requests
from bs4 import BeautifulSoup

url = "https://www.drdo.gov.in/drdo/offerings/vacancies"

response = requests.get(url)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

text = soup.get_text()

print(text[:3000])
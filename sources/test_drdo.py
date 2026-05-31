import requests
from bs4 import BeautifulSoup

url = "https://www.drdo.gov.in/drdo/offerings/vacancies"

response = requests.get(url)

print("Status:", response.status_code)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

print("Title:")
print(soup.title.text)
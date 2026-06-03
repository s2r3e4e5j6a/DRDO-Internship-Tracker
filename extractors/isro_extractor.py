import requests
from bs4 import BeautifulSoup

url = "https://www.isro.gov.in/START2026.html"

response = requests.get(url)

print("Status:", response.status_code)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

print("\nTITLE:\n")

print(soup.title.text)

print("\nPAGE TEXT:\n")

text = soup.get_text(
    separator="\n",
    strip=True
)

print(text[:5000])
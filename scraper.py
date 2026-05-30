import requests
from bs4 import BeautifulSoup

url = "https://www.drdo.gov.in"

response = requests.get(url)

print("Status Code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

print("\nWebsite Title:")
print(soup.title.text)
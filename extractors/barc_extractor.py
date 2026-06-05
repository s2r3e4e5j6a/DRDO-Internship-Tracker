import requests
from bs4 import BeautifulSoup

url = "https://www.barc.gov.in/student/index.html"
response = requests.get(url)

print("Status:", response.status_code)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

print("\nHEADINGS\n")

for heading in soup.find_all(
    ["h1", "h2", "h3", "h4"]
):

    text = heading.get_text(
        strip=True
    )

    if text:

        print(text)

print("\nRECRUITMENT LINKS\n")

for link in soup.find_all("a"):

    text = link.get_text(strip=True)

    href = link.get("href")

    if text and href:

        print(text, "->", href)
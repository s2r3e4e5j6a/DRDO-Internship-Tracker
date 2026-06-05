import requests
from bs4 import BeautifulSoup

url = "https://www.drdo.gov.in/drdo/en/offerings/vacancies/mtrdc-bengalure-invites-applications-paid-internship-scheme-2026-27-pursuing"
print(url)
response = requests.get(
    url,
    timeout=20
)
print("Status:", response.status_code)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)
print("\nPDF LINKS\n")

for link in soup.find_all("a"):

    text = link.get_text(strip=True)

    href = link.get("href")

    if href and ".pdf" in href.lower():

        print(text, "->", href)
print("\nTITLE:\n")

if soup.title:
    print(soup.title.text)

print("\nTEXT:\n")

print(
    soup.get_text(
        separator="\n",
        strip=True
    )[:5000]
)
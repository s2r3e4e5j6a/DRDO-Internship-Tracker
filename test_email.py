from utils.email_sender import send_email
import requests
from bs4 import BeautifulSoup

# =========================
# SEND TEST EMAIL
# =========================

success = send_email(
    "Test Alert",
    "New opportunity detected!"
)

if success:
    print("✅ Email test passed.")
else:
    print("❌ Email test failed.")

# =========================
# TEST WEBSITE SCRAPING
# =========================

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

    print("\nLINKS FOUND\n")

    for link in soup.find_all("a"):

        text = link.get_text(
            strip=True
        )

        href = link.get("href")

        if text and href:

            print(
                text,
                "->",
                href
            )

except Exception as e:

    print(
        f"Website Error: {e}"
    ) 
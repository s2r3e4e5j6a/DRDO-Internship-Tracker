import pdfplumber
import re

with pdfplumber.open(
    "mtrdc.pdf"
) as pdf:

    text = ""

    for page in pdf.pages:

        page_text = page.extract_text()

        if page_text:

            text += page_text + "\n"

print("\nELIGIBILITY FOUND\n")

matches = re.findall(
    r"final year.*",
    text,
    re.IGNORECASE
)

for match in matches:

    print(match)
duration = "Unknown"

if "Six months" in text:
    duration = "6 Months"

eligibility = "Unknown"

matches = re.findall(
    r"final year.*",
    text,
    re.IGNORECASE
)

if matches:
    eligibility = matches[0]

print("Eligibility:", eligibility)
print("Duration:", duration)
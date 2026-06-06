import pdfplumber
import re


def extract_pdf_details(pdf_path):

    text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text + "\n"

    eligibility = "Unknown"

    matches = re.findall(
        r"final year.*",
        text,
        re.IGNORECASE
    )

    if matches:

        eligibility = matches[0]

    duration = "Unknown"

    if "Six months" in text:

        duration = "6 Months"

    return {
        "Eligibility": eligibility,
        "Duration": duration
    }
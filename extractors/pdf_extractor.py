import requests

pdf_url = (
    "https://www.drdo.gov.in/drdo/sites/default/files/"
    "vacancy/advtMTRDC22052026.pdf"
)

response = requests.get(
    pdf_url,
    timeout=20
)

with open(
    "mtrdc.pdf",
    "wb"
) as f:

    f.write(response.content)

print(
    "PDF Downloaded Successfully"
)
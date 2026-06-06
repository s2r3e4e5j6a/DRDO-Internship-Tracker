import pdfplumber

all_text = ""

with pdfplumber.open(
    "yuvika.pdf"
) as pdf:

    for page in pdf.pages:

        text = page.extract_text()

        if text:

            all_text += text + "\n"

with open(
    "yuvika_text.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(all_text)

print(
    "Text Extracted Successfully"
)

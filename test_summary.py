from utils.summarizer import summarize_opportunity

sample = {
    "Lab": "START 2026",
    "Source": "ISRO",
    "Deadline": "2026-02-13",
    "Eligibility": "PG and Final-Year UG Students",
    "Location": "Online"
}

print(
    summarize_opportunity(sample)
)
import pandas as pd

data = {
    "Lab": ["DRDL", "VRDE", "MTRDC"],
    "Location": ["Hyderabad", "Maharashtra", "Bengaluru"],
    "Deadline": ["2026-06-15", "2026-06-10", "2026-06-20"],
    "Status": ["Open", "Closing Soon", "Open"]
}

df = pd.DataFrame(data)

df.to_csv("data/internships.csv", index=False)

print("CSV updated successfully")
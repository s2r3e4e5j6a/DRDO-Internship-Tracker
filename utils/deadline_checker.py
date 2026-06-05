import pandas as pd


def get_urgent_opportunities():

    df = pd.read_csv(
        "data/internships.csv"
    )

    df["Deadline"] = pd.to_datetime(
        df["Deadline"],
        errors="coerce"
    )

    today = pd.Timestamp.today()

    df["Days Left"] = (
        df["Deadline"] - today
    ).dt.days

    urgent = df[
        (df["Days Left"] >= 0)
        &
        (df["Days Left"] <= 7)
    ]

    return urgent


if __name__ == "__main__":

    urgent = get_urgent_opportunities()

    print(urgent)
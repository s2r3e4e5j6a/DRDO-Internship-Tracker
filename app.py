import streamlit as st
import pandas as pd
import subprocess

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="DRDO Internship Tracker",
    page_icon="🚀",
    layout="wide"
)
if st.button("🔄 Refresh Internship Data"):

    subprocess.run(
        ["python", "scraper.py"]
    )

    st.success(
        "Internship data updated!"
    )
if st.button("📧 Send Internship Report"):

    import email_alert

    st.success(
        "Internship report sent!"
    )
# ==========================
# LOAD DATA
# ==========================

df = pd.read_csv("data/internships.csv")
if "Status" not in df.columns:
    df["Status"] = "Open"

df["Status"] = df["Status"].fillna("Open")
source_filter = st.selectbox(
    "Filter by Organization",
    ["All", "DRDO", "ISRO", "BARC"]
)

df["Deadline"] = pd.to_datetime(df["Deadline"])

today = pd.Timestamp.today().normalize()

df["Days Left"] = (df["Deadline"] - today).dt.days

# ==========================
# TITLE
# ==========================

st.title("🚀 DRDO Internship Tracker")

# ==========================
# ADD INTERNSHIP
# ==========================

st.subheader("Add New Internship")

with st.form("internship_form"):

    lab = st.text_input("Lab Name")

    location = st.text_input("Location")

    deadline = st.date_input("Deadline")

    submit = st.form_submit_button("Add Internship")

if submit:

    days_left = (
        pd.to_datetime(deadline)
        - pd.Timestamp.today()
    ).days

    if days_left <= 15:
        status = "Closing Soon"
    else:
        status = "Open"

    new_row = pd.DataFrame({
        "Lab": [lab],
        "Location": [location],
        "Deadline": [deadline],
        "Status": [status],
        "Source": ["Manual Entry"]
    })

    df_save = pd.read_csv(
        "data/internships.csv"
    )

    df_save = pd.concat(
        [df_save, new_row],
        ignore_index=True
    )

    df_save.to_csv(
        "data/internships.csv",
        index=False
    )

    st.success(
        "✅ Internship Added Successfully!"
    )

# ==========================
# SEARCH
# ==========================

search = st.text_input(
    "Search by Lab or Location"
)

# ==========================
# FILTER
# ==========================

status_filter = st.selectbox(
    "Filter by Status",
    ["All", "Open", "Closing Soon"]
)

filtered_df = df.copy()
if source_filter != "All":
    filtered_df = filtered_df[
        filtered_df["Source"] == source_filter
    ]

if search:

    filtered_df = filtered_df[
        filtered_df["Lab"].str.contains(
            search,
            case=False,
            na=False
        )
        |
        filtered_df["Location"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

if status_filter != "All":

    filtered_df = filtered_df[
        filtered_df["Status"] == status_filter
    ]

# ==========================
# TABLE
# ==========================

st.subheader("Available Internships")

display_df = filtered_df.copy()

display_df["Status"] = display_df["Status"].replace({
    "Open": "🟢 Open",
    "Closing Soon": "🟠 Closing Soon"
})

st.dataframe(display_df)

# ==========================
# URGENT DEADLINES
# ==========================

urgent = df[df["Days Left"] <= 15]

if not urgent.empty:

    st.warning(
        "⚠ Internships Closing Soon!"
    )

    st.dataframe(
        urgent[
            ["Lab", "Deadline", "Days Left"]
        ]
    )

# ==========================
# DASHBOARD SUMMARY
# ==========================

st.subheader("Dashboard Summary")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total Internships",
        len(df)
    )

with col2:
    st.metric(
        "Open Positions",
        len(
            df[df["Status"] == "Open"]
        )
    )
# ==========================
# CHARTS
# ==========================


st.subheader("Internships by Location")

location_counts = df["Location"].value_counts()

st.bar_chart(location_counts)
# ==========================
# DOWNLOAD CSV
# ==========================

st.subheader("Download Data")

csv = df.to_csv(index=False)

st.download_button(
    label="⬇ Download Internship Data",
    data=csv,
    file_name="internships.csv",
    mime="text/csv"
)
# ==========================
# DELETE INTERNSHIP
# ==========================

st.subheader("Delete Internship")

lab_to_delete = st.selectbox(
    "Select Lab to Delete",
    df["Lab"].unique()
)

if st.button(
    "Delete Selected Internship"
):

    df_updated = df[
        df["Lab"] != lab_to_delete
    ]

    df_updated.to_csv(
        "data/internships.csv",
        index=False
    )

    st.success(
        f"✅ {lab_to_delete} deleted successfully!"
    )
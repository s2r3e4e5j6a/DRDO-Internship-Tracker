import schedule
import time
import subprocess


def run_checks():

    print(
        "\nRunning internship checks..."
    )

    subprocess.run(
        ["python", "check_new_opportunities.py"]
    )

    subprocess.run(
        ["python", "deadline_alert.py"]
    )


schedule.every(1).minutes.do(
    run_checks
)

print(
    "Scheduler started..."
)

while True:

    schedule.run_pending()

    time.sleep(1)
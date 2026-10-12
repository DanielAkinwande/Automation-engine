import os

from tasks.file_ops import rename_files, move_files
from tasks.report import generate_report
from tasks.emailer import send_email

SOURCE = "data/source"
DEST = "data/destination"

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")


def run_engine():
    result = {"steps": []}
    print("Running automation...")

    try:
        rename_files(SOURCE)
        result["steps"].append("Files renamed")

        move_files(SOURCE, DEST)
        result["steps"].append("Files moved")

        report_path = generate_report(DEST)

        send_email(report_path, EMAIL, PASSWORD, RECEIVER)
        result["steps"].append("Email sent!")

        result["status"] = "success"

    except Exception as e:
        result["steps"].append(f"Error: {str(e)}")
        result["status"] = "Error"

    return result

print("Done.\n")

def log(message):
    with open("app.log", "a") as f:
        f.write(message + "\n")

if __name__ == "__main__":
    run_engine()
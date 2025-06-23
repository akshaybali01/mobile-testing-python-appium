import pytest
import json
from datetime import datetime
import webbrowser
import os

from generate_dashboard import generate_dashboard
from utilities.result_logger import log_test_result

# Ensure reports folder exists
os.makedirs("reports", exist_ok=True)

# Step 1: Create timestamped report names
timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
html_report = f"reports/report_{timestamp}.html"
json_report = f"reports/report_{timestamp}.json"

# Step 2: Run Pytest with HTML + JSON report output
result = pytest.main([
    "tests",
    f"--html={html_report}",
    "--self-contained-html",
    "--json-report",
    f"--json-report-file={json_report}",
    "-v",
    "--capture=tee-sys",

])

# Step 3: Status based on return code
status = "Passed" if result == 0 else "Failed"

# Step 4: Extract stats from JSON report
def extract_stats_from_json(json_path):
    try:
        with open(json_path, "r") as f:
            data = json.load(f)
            summary = data.get("summary", {})
            return (
                summary.get("total", "NA"),
                summary.get("passed", "NA"),
                summary.get("failed", "NA"),
                summary.get("skipped", "NA")
            )
    except Exception as e:
        print(f"Error reading JSON report: {e}")
        return "NA", "NA", "NA", "NA"

total, passed, failed, skipped = extract_stats_from_json(json_report)

# Step 5: Log results to CSV
log_test_result(status, total, passed, failed, skipped, html_report)

# Step 6: Generate dashboard
generate_dashboard()

# Step 7: Auto open dashboard
#webbrowser.open("reports/dashboard.html")

print("Test run completed.")

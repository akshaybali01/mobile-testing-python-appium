import csv
import os
from datetime import datetime

def log_test_result(status,total,passed,failed,skipped,report_path):
    timestamp=datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    log_path="reports/test_history.csv"
    os.makedirs("reports",exist_ok=True)

    #Only writes the CSV column headers if the file is being created for the first time.
    write_header= not os.path.exists(log_path)

    with open(log_path,mode='a',newline='') as file:
        writer=csv.writer(file)
        if write_header:
            writer.writerow(["Timestamp","Status","Total","Passed","Failed","Skipped","Report"])
        writer.writerow([timestamp,status,total,passed,failed,skipped,report_path])

import csv
import os


def generate_dashboard(csv_path="reports/test_history.csv", output_path="reports/dashboard.html"):
    if not os.path.exists(csv_path):
        print(" ❌ CSV log not found")
        return

    rows = []

    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rows.append(row)

    # HTML structure
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Test Execution Dashboard</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: #f4f4f4; }
            h1 { text-align: center; }
            table { border-collapse: collapse; width: 100%; background: #fff; box-shadow: 0 0 10px; }
            th, td { border: 1px solid #ddd; padding: 10px; text-align: center; }
            th { background-color: #444; color: white; }
            tr:nth-child(even) { background-color: #f2f2f2; }
            .Passed { background-color: #c8e6c9; font-weight: bold; }
            .Failed { background-color: #ffcdd2; font-weight: bold; }
        </style>
    </head>
    <body>
        <h1> 🏠 Test Execution Dashboard</h1>
        <table>
            <tr>
                <th>Timestamp</th>
                <th>Status</th>
                <th>Total</th>
                <th>Passed</th>
                <th>Failed</th>
                <th>Skipped</th>
                <th>Report</th>
            </tr>
    """

    for row in rows:
        status_class = "Passed" if row["Status"] == "Passed" else "Failed"
        html += f"""
            <tr>
                <td>{row['Timestamp']}</td>
                <td class="{status_class}">{row['Status']}</td>
                <td>{row['Total']}</td>
                <td>{row['Passed']}</td>
                <td>{row['Failed']}</td>
                <td>{row['Skipped']}</td>
                <td><a href="{os.path.basename(row['Report'])}" target="_blank">View Report</a></td>




            </tr>
        """

    html += """
        </table>
    </body>
    </html>
    """

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ Dashboard generated at: {output_path}")


if __name__ == "__main__":
    generate_dashboard()

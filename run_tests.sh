#!/bin/bash
# Set timestamp and report filename
timestamp=$(date + "%Y-%m-%d-%H-%M-%S")
report_file="reports/report_$timestamp.html"

echo " 🚀 Running tests and saving report to $report_file"
# Run pytest with smoke marker and report options
pytest -m smoke --html="$report_file" --self-contained-html -v -s

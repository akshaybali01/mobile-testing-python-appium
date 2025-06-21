import pytest
from _pytest.reports import TestReport
from appium import webdriver
import os
import pytest
from datetime import datetime

from drivers.appium_driver import create_driver
from pytest_html import extras  # Make sure pytest-html is installed

from utilities.appium_service_util import start_appium, stop_appium

@pytest.fixture(scope="session",autouse=True)
def appium_server():
    start_appium()
    print("Appium server is auto-started!")
    yield
    stop_appium()




# @pytest.fixture(scope="session")
# def driver(request):
#     config_path = request.config.getoption("--device")
#     if not config_path:
#         pytest.exit("❌ Please provide --device=config/device1.json")
#
#     driver = create_driver(config_path)
#     yield driver
#     driver.quit()




# this was for single device
@pytest.fixture(scope="function")
def driver():
    driver = create_driver()
    yield driver
    driver.quit()


# @pytest.fixture(params=[
#     "config/device1.json",
#     "config/device2.json"
# ],scope="session")
# def driver(request):
#     driver = create_driver(request.param)
#     yield driver
#     driver.quit()

# Pytest hook to add screenshots to report on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report: TestReport = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"{item.name}_{timestamp}.png"
            screenshot_path = os.path.join(screenshots_dir, file_name)

            driver.save_screenshot(screenshot_path)

            # Embed screenshot in HTML report
            extra = getattr(report, "extra", [])
            if os.path.exists(screenshot_path):
                relative_path = os.path.relpath(screenshot_path, start="reports")
                html = f'<div><img src="{relative_path}" alt="screenshot" style="width:300px;height:auto;" onclick="window.open(this.src)" /></div>'
                extra.append(extras.html(html))
            report.extra = extra

def pytest_addoption(parser):
    parser.addoption(
        "--device",
        action="store",
        default=None,
        help="Device config JSON file path (e.g. config/device1.json)"
    )
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment: dev or prod or staging"
    )


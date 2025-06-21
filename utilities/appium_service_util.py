from appium.webdriver.appium_service import AppiumService

from utilities.logger_util import create_logger

appium_service = AppiumService()
logger = create_logger("appium service")
def start_appium():
    if not appium_service.is_running:
        appium_service.start(args=["--port","4723"])
        logger.info("[Appium] started on port 4723")
def stop_appium():
    if appium_service.is_running:
        appium_service.stop()
        logger.info("[Appium] stoped!")
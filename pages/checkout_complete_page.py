import time

from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class CheckoutCompletePage(BasePage):
    TITLE = (AppiumBy.ACCESSIBILITY_ID, "test-CHECKOUT: COMPLETE!")
    THANK_YOU_MSG = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'THANK')]")

    def is_checkout_complete_page_displayed(self):
        self.wait_for_element(self.TITLE)
        return self.is_displayed(self.TITLE)

    def is_order_complete(self):
        self.wait_for_element(self.THANK_YOU_MSG)
        print("success message: ",self.get_text(self.THANK_YOU_MSG))
        return self.get_text(self.THANK_YOU_MSG)


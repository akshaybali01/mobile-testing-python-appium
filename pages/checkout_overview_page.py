from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver

class CheckoutOverviewPage(BasePage):
    TITLE = (AppiumBy.ACCESSIBILITY_ID, "test-CHECKOUT: OVERVIEW")
    FINISH_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "test-FINISH")

    def is_checkout_overviewpage_displayed(self):
        self.wait_for_element(self.TITLE)
        return self.is_displayed(self.TITLE)

    def navigate_to_checkout_complete_page(self):
        max_swipes=10
        swipe_count=0
        while swipe_count<max_swipes:
            element = self.driver.find_elements(*self.FINISH_BUTTON)
            if element:
                break
            self.swipe_up()

        self.click(self.FINISH_BUTTON)



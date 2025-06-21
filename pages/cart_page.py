from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class CartPage(BasePage):
    TITLE=(AppiumBy.XPATH,"//android.widget.TextView[@text='YOUR CART']")
    CHECKOUT_BUTTON=(AppiumBy.ACCESSIBILITY_ID,"test-CHECKOUT")

    def is_cart_page_displayed(self):
        self.wait_for_element(self.TITLE)
        return self.is_displayed(self.TITLE)

    def click_checkout_button(self):
        self.click(self.CHECKOUT_BUTTON)
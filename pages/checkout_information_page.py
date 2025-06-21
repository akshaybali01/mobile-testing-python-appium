from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class CheckoutInformationPage(BasePage):
    FIRSTNAME_FIELD=(AppiumBy.ACCESSIBILITY_ID,"test-First Name")
    LASTNAME_FIELD=(AppiumBy.ACCESSIBILITY_ID,"test-Last Name")
    ZIP_FIELD = (AppiumBy.ACCESSIBILITY_ID,"test-Zip/Postal Code")
    CONTINUE_BUTTON= (AppiumBy.ACCESSIBILITY_ID,"test-CONTINUE")

    def enter_user_info(self,firstname,lastname,zip_code):
        self.wait_for_element(self.FIRSTNAME_FIELD)
        self.click_and_send_keys(self.FIRSTNAME_FIELD,firstname)
        self.click_and_send_keys(self.LASTNAME_FIELD, lastname)
        self.click_and_send_keys(self.ZIP_FIELD, zip_code)
        self.driver.hide_keyboard()

    def navigate_to_checkoutoverview_page(self):
        self.click(self.CONTINUE_BUTTON)


from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class LoginPage(BasePage):

    USERNAME_FIELD=(AppiumBy.ACCESSIBILITY_ID, "test-Username")
    PASSWORD_FIELD = (AppiumBy.ACCESSIBILITY_ID, "test-Password")
    LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")
    ERROR_MESSAGE_LOCKED_USER=(AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'locked out')]")

    def login(self,username,password):
        self.wait_for_element(self.USERNAME_FIELD)
        print(f'Login with {username} and {password}')
        self.click_and_send_keys(self.USERNAME_FIELD,username)
        self.click_and_send_keys(self.PASSWORD_FIELD,password)
        self.click(self.LOGIN_BUTTON)

    def get_error_messgae(self):
        self.wait_for_element(self.ERROR_MESSAGE_LOCKED_USER)
        text= self.get_text(self.ERROR_MESSAGE_LOCKED_USER)
        print('Locked Text error message:',text)
        return text

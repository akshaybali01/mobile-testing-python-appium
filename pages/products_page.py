from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class ProductsPage(BasePage):

    TITLE=(AppiumBy.XPATH,"//android.widget.TextView[@text='PRODUCTS']")
    ADD_FIRST=(AppiumBy.XPATH,"(//android.view.ViewGroup[@content-desc='test-ADD TO CART'])[1]")
    CART_ICON=(AppiumBy.ACCESSIBILITY_ID,"test-Cart")

    def is_product_page_displayed(self):
        self.wait_for_element(self.TITLE)
        return self.is_displayed(self.TITLE)

    def add_first_product_to_cart(self):
        self.click(self.ADD_FIRST)

    def go_to_cart(self):
        self.click(self.CART_ICON)

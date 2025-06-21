from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_add_to_cart(driver):
    LoginPage(driver).login("standard_user","secret_sauce")
    product_page =ProductsPage(driver)
    assert product_page.is_product_page_displayed()
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    assert CartPage(driver).is_cart_page_displayed()

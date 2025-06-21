import pytest

from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_information_page import CheckoutInformationPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utilities.csv_util import read_csv
from utilities.logger_util import create_logger

logger = create_logger("test_checkout")

test_data =read_csv("data/checkout_data.csv")

@pytest.mark.smoke
@pytest.mark.parametrize("data",test_data)
def test_checkout_flow(driver,data):
    first_name=data["firstname"]
    last_name=data["lastname"]
    zip_code=data["postal_code"]
    logger.info(f"Start checkout test with {first_name} {last_name}")
    logger.info("Test started: Checkout Flow..")
    login_page=LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)
    assert products_page.is_product_page_displayed(),"login failed"

    #products page
    products_page.add_first_product_to_cart()
    products_page.go_to_cart()

    # Cart Page
    cart_page=CartPage(driver)
    assert cart_page.is_cart_page_displayed(),"cart page not loaded"
    cart_page.click_checkout_button()

    # Checkout Info
    checkout_info =CheckoutInformationPage(driver)
    checkout_info.enter_user_info(first_name, last_name, zip_code)
    checkout_info.navigate_to_checkoutoverview_page()

    # Checkout Overview
    checkout_overview =CheckoutOverviewPage(driver)
    assert checkout_overview.is_checkout_overviewpage_displayed(),"checkout Overview page is not loaded"
    checkout_overview.navigate_to_checkout_complete_page()

    ## Checkout Complete
    checkout_complete = CheckoutCompletePage(driver)
    assert checkout_complete.is_checkout_complete_page_displayed,"checkout complete page is not loaded"
    logger.info("Checkout complete page is lodded successfully")
    assert "thank you" in checkout_complete.is_order_complete().lower()
    logger.info("Check out test is complete now. ")



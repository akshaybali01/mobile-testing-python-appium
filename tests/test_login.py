from pages.login_page import LoginPage
from pages.products_page import ProductsPage
import pytest

from utilities.csv_util import read_csv
from utilities.logger_util import create_logger

# @pytest.mark.parametrize("username,password,expected",[
#     ("standard_user","secret_sauce",True),
#     #("problem_user","secret_sauce"),
#     ("locked_out_user","secret_sauce",False)
# ])

# load data once
logger = create_logger(__name__)

test_data = read_csv("data/login_data.csv")

@pytest.mark.smoke
@pytest.mark.parametrize("data", test_data)
def test_valid_login(driver, data):
    username = data["username"]
    password = data["password"]
    expected = data["expected_result"]

    login_page = LoginPage(driver)
    login_page.login(username, password)

    if expected=='success':
        assert ProductsPage(driver).is_product_page_displayed(),f"Login failed with {username}"
    else:
        error_message= login_page.get_error_messgae().lower()
        logger.info(f"Here is the error message for locked user {error_message}")
        assert "akshay" in login_page.get_error_messgae().lower()

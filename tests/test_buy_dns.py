import time
import allure
import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from pages.phone2023_page import Phone2023_page
from pages.cart_page import Cart_page
from pages.confirmation import Confirmation_page
from pages.filters_page import Filters_page
from pages.login_page_my import Login_page
from pages.smartphone_page import Smartphone_page


@pytest.mark.run(order=1)
@allure.description("Test buy dns")
def test_buy_dns(set_up, set_grow):

    """Testing the functionality of the DNS site with the following steps:
    --
    1) Authorization.
    2) The choice in the product catalog is a smartphone.
    3) Choosing a smartphone in 2023.
    4) Filter selection: Rating 4 and higher, There is an overview, Transition to all filters, the number of pixels of the main camera from 100.
    5) Smartphone Selection: Realme 10 Pro 5G 128GB blue smartphone.
    6) Go to the shopping cart.
    7) Transition to the design.
    8) Entering the number.
    9) Remove the marker-tick "PROZAPASS".
    10) Confirm the order."""

    #   OPTOINS
    options = webdriver.ChromeOptions()

    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36")

    options.add_argument("--disable-blink-features=AutomationControlled")

    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities["pageLoadStrategy"] = "eager"

    s = Service(executable_path=r"utilities/chromedriver.exe")
    driver = webdriver.Chrome(service=s, options=options, desired_capabilities=capabilities)

    #   AUTHORIZATION
    lp = Login_page(driver)
    lp.authorization()

    #   SELECT SMARTPHONE
    sp = Smartphone_page(driver)
    sp.select_smartphones()

    #   SELECT PHONE 2023
    ph = Phone2023_page(driver)
    ph.select_phone2023()

    #   FILTERS
    fp = Filters_page(driver)
    fp.filters()

    #   CART
    cp = Cart_page(driver)
    cp.cart()

    #   CONFIRMATION
    con = Confirmation_page(driver)
    con.confirmation()


    time.sleep(5)
    driver.close()
    driver.quit()
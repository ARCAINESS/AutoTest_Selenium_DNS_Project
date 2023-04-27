import time
import allure
import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from pages.Phone2023_page import Phone2023_page
from pages.cart_page import Cart_page
from pages.confirmation import Confirmation_page
from pages.filters_page import Filters_page
from pages.login_page_my import Login_page
from pages.smartphone_page import Smartphone_page


@pytest.mark.run(order=1)
@allure.description("Test buy dns")
def test_buy_dns(set_up, set_grow):

    #   OPTOINS
    options = webdriver.ChromeOptions()

    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36")

    options.add_argument("--disable-blink-features=AutomationControlled")

    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities["pageLoadStrategy"] = "eager"

    s = Service(executable_path=r"C:\Users\serge\PycharmProjects\resource\chromedriver.exe")
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
import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Phone2023_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #   LOCATORS

    phone2023_button = "//a[contains(text(),'Смартфоны')]/following-sibling::a[contains(text(),'2023')]"


    #   GETTERS

    def get_phone2023_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.phone2023_button)))


    #   ACTIONS

    def click_phone2023_button(self):
        self.get_phone2023_button().click()
        print("Click phone2023 button")


    #   METHODS

    def select_phone2023(self):
        with allure.step("Select phone2023 button"):
            Logger.add_start_step(method="select_phone2023")
            self.get_current_url()
            self.click_phone2023_button()
            self.assert_url("https://www.dns-shop.ru/catalog/recipe/3907bff298e20bb0/2023-goda/")
            Logger.add_end_step(url=self.driver.current_url, method="select_phone2023")
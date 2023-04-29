import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Smartphone_page(Base):


    #   LOCATORS

    cataloge_button = "//span[@data-role='catalog-button']"
    smartphone_button = "//span[contains(text(),'Смартфоны и фототехника')]"


    #   GETTERS

    def get_cataloge_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cataloge_button)))

    def get_smartphone_button(self):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, self.smartphone_button)))


    #   ACTIONS

    def click_cataloge_button(self):
        self.get_cataloge_button().click()
        print("Click cataloge button")

    def click_smartphone_button(self):
        self.get_smartphone_button().click()
        print("Click smartphone button")


    #   METHODS

    def select_smartphones(self):
        with allure.step("Select smartphones"):
            Logger.add_start_step(method="select_smartphones")
            self.get_current_url()
            self.click_cataloge_button()
            self.click_smartphone_button()
            self.assert_url("https://www.dns-shop.ru/catalog/17a890dc16404e77/smartfony-i-fototexnika/")
            Logger.add_end_step(url=self.driver.current_url, method="select_smartphones")
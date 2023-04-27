import time
import allure
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Cart_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #   LOCATORS

    name_smartphone = "//a[contains(text(),'Смартфон')]"
    checkout_button = "//span[contains(text(),'Перейти')]"
    checkout_button_another = "//div[contains(@class,'total-amount__buttons-section')]//button[contains(@class,'buy-button')]"


    #   GETTERS

    def get_name_smartphone(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.name_smartphone)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def get_checkout_button_another(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button_another)))


    #   ACTIONS

    def click_checkout_button(self):
        try:
            action = ActionChains(self.driver)
            action.move_to_element(self.get_checkout_button()).perform()
            self.get_checkout_button().click()
            print("Click checkout button")
        except TimeoutException:
            action = ActionChains(self.driver)
            action.move_to_element(self.get_checkout_button_another()).perform()
            self.get_checkout_button_another().click()
            print("Click checkout button another")


    #   METHODS

    def cart(self):
        with allure.step("Cart"):
            Logger.add_start_step(method="cart")
            self.get_current_url()
            self.assert_word(self.get_name_smartphone(), '6.72" Смартфон realme 10 Pro 5G 128 ГБ голубой')
            self.get_screenshot()
            self.click_checkout_button()
            Logger.add_end_step(url=self.driver.current_url, method="cart")
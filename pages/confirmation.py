import time
import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger
from utilities.auth_data import mail_number



class Confirmation_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #   LOCATORS

    remove_check_mark = "//label[contains(@class,'checkbox_g93')]"
    number = "//input[@type='tel']"
    confirmation_button = "//span[contains(text(),'Подтвердить заказ')]"
    proof_number = "//div[contains(text(),'На номер ')]//br"


    #   GETTERS

    def get_remove_check_mark(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.remove_check_mark)))

    def get_number(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.number)))

    def get_confirmation_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.confirmation_button)))

    def get_proof_number(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.proof_number)))


    #   ACTIONS

    def click_remove_check_mark(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_remove_check_mark()).perform()
        self.get_remove_check_mark().click()
        print("Click remove check mark button")

    def input_number(self, number):
        self.get_number().send_keys(number)
        print("Input number")

    def click_confirmation_button(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_confirmation_button()).perform()
        self.get_confirmation_button().click()
        print("Click confirmation button")


    #   METHODS

    def confirmation(self):
        with allure.step("Confirmation"):
            Logger.add_start_step(method="confirmation")
            self.get_current_url()
            self.input_number(mail_number)
            self.click_remove_check_mark()
            self.click_confirmation_button()
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="confirmation")
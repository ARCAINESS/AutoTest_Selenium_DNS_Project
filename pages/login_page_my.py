import allure
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.auth_data import mail_login, mail_password
from utilities.logger import Logger


class Login_page(Base):


    url = "https://www.dns-shop.ru/profile/menu/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #   LOCATORS

    enter_button = "//button[@class='button-ui button-ui_white user-page__login-btn']"
    with_password_button = "//div[@class='block-other-login-methods__password-caption']"
    user_name = "//input[(@autocomplete='username')]"
    password = "//input[(@type='password')]"
    login_button = "//button[contains(@class,'base-ui-button-v2_big')]"
    assert_word_HO34765 = "//a[contains(text(),'HO34765')]"


    #   GETTERS

    def get_enter_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_with_password_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.with_password_button)))

    def get_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_assert_word_HO34765(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.assert_word_HO34765)))




    #   ACTIONS

    def click_enter_button(self):
        self.get_enter_button().click()
        print("Click enter button")

    def click_with_password_button(self):
        self.get_with_password_button().click()
        print("Click with password button")
        time.sleep(2)

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    #   IF MISTAKE
    def restart_authorization(self):
        print("Authorization Mistake")
        self.driver.refresh()
        self.click_enter_button()
        self.click_with_password_button()
        self.input_user_name(mail_login)
        self.input_password(mail_password)
        self.click_login_button()
        self.assert_word(self.get_assert_word_HO34765(), "Пришелец-HO34765")


    #   METHODS

    def authorization(self):

        with allure.step("Authorization"):
            Logger.add_start_step(method="authorization")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_enter_button()
            self.click_with_password_button()
            self.input_user_name(mail_login)
            self.input_password(mail_password)
            self.click_login_button()
            try:
                self.assert_word(self.get_assert_word_HO34765(), "Пришелец-HO34765")
            except TimeoutException:
                self.restart_authorization()

            self.assert_url("https://www.dns-shop.ru/profile/menu/")
            Logger.add_end_step(url=self.driver.current_url, method="authorization")

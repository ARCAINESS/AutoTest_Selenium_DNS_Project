import time
import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Filters_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #   LOCATORS

    rating_4_and_higher = "//div[@data-id='rating']"
    review_on = "//div[@data-id='review']"
    all_filters = "//a[@data-role='extended-filters-link']"
    pixels_camera = "//span[contains(text(),'Количество мегапикселей основной камеры (Мп)')]"
    entry_pixels = "//span[contains(text(),'9.1 - 14  ')]/ancestor::div[contains(@class,'ui-collapse__content ui-collapse__content_list ui-collapse__content_in')]//input[contains(@class,'ui-input-small__input ui-input-small__input_list')]"
    buy_phone = "//div[@data-product='4d1f1278-953a-11ed-9082-00155d8ed20c']//button[contains(text(),'Купить')]"
    cart = "//button[contains(text(),'В корзине')]"

    #   GETTERS

    def get_rating_4_and_higher(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.rating_4_and_higher)))

    def get_review_on(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.review_on)))

    def get_all_filters(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.all_filters)))

    def get_pixels_camera(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.pixels_camera)))

    def get_entry_pixels(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.entry_pixels)))

    def get_buy_phone(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.buy_phone)))

    def get_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart)))


    #   ACTIONS

    def click_rating_4_and_higher(self):
        self.get_rating_4_and_higher().click()
        print("Click rating 4 and higher")

    def click_review_on(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_review_on()).perform()
        self.get_review_on().click()
        print("Click review 'ON'")

    def click_all_filters(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_all_filters()).perform()
        self.get_all_filters().click()
        print("Click all filters")

    def click_pixels_camera(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_pixels_camera()).perform()
        self.get_pixels_camera().click()
        print("Click pixels camera")

    def input_pixels(self, pixels):
        self.get_entry_pixels().send_keys(pixels)
        print("Entering the number of pixels")

    def click_enter(self):
        self.get_entry_pixels().send_keys(Keys.RETURN)
        print("Click enter")

    def click_buy_phone(self):
        try:
            action = ActionChains(self.driver)
            action.move_to_element(self.get_buy_phone()).perform()
            self.get_buy_phone().click()
            print("Click buy phone")
        except TimeoutException:
            print("THE PRODUCT IS ALREADY IN THE CART")
            pass

    def go_to_cart(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_cart()).perform()
        self.get_cart().click()
        print("Go to cart")

    #   METHODS

    def filters(self):
        with allure.step("Filters"):
            Logger.add_start_step(method="filters")
            self.get_current_url()
            self.click_rating_4_and_higher()
            self.click_review_on()
            self.click_all_filters()
            self.click_pixels_camera()
            self.input_pixels(pixels="100")
            self.get_screenshot()
            self.click_enter()
            self.click_buy_phone()
            self.go_to_cart()
            Logger.add_end_step(url=self.driver.current_url, method="filters")
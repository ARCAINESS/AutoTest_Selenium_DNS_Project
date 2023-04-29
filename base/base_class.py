import datetime


class Base():


    def __init__(self, driver):
        self.driver = driver

    """GET CURRENT URL"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url : " + get_url)

    """ASSERT PRODUCTS WORD"""
    def assert_word(self, word, result):
        value_assert_word = word.text
        assert value_assert_word == result
        print("Success Assert Word")

    """SCREENSHOT"""
    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%m.%d.%H.%M.%S")
        name_screenshot = f"Screen{now_date}.png"
        self.driver.save_screenshot(fr"screen\{name_screenshot}")
        print("Get Screenshot")

    """ASSERT URL"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Success URL Assert")
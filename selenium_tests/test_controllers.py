from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Test_Controllers:

    @classmethod
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

    # @classmethod
    # def teardown(cls):
    #     driver.quit()

    def test_login(self):
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        driver.get_screenshot_as_file(
            "C:/Users/AlexKuzmin/PycharmProjects/TestCases/selenium_tests/screen_shot/sauce1.jpg")

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest


class TestSample1:

    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://stage.supplant.me/home/dashboard")
        driver.maximize_window()
        yield
        driver.quit()

    def test_demo1(self, test_setup):
        print("\n")
        print("Title is: " + driver.title)
        print("URL is: " + driver.current_url)

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Test_WebDriverMethods:

    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://google.com")
        yield
        driver.quit()

    def test_demo_1(self, test_setup):
        print("\n")
        print("This is title: " + driver.title)
        print("This is current url: " + driver.current_url)
        # print("This is page source: " + driver.page_source)
        driver.get_screenshot_as_file("C:/Users/AlexKuzmin/PycharmProjects/TestCases/selenium_tests/screen_shot/img1.jpg")
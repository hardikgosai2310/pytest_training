from assertpy import assert_that
from selenium import webdriver


# url = https://opensource-demo.orangehrmlive.com/
# title = 'OrangeHRM'

class TestLoginUI:
    def test_title(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get('https://opensource-demo.orangehrmlive.com/')
        actual_title = driver.title
        assert actual_title == 'OrangeHRM'
        assert_that('OrangeHRM').is_equal_to(actual_title)

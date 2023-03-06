import time

import pytest
from assertpy import assert_that
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin:
    @pytest.fixture(scope="function", autouse=True)
    def browser_config(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        yield
        self.driver.quit()

    def test_valid_login(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        actual_text = self.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text
        assert_that("Dashboard").is_equal_to(actual_text)


class TestLoginUI:
    @pytest.fixture(scope='function')
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('https://opensource-demo.orangehrmlive.com/')

        yield
        time.sleep(3)
        self.driver.quit()

    def test_title(self, setup):
        actual_title = self.driver.title
        assert actual_title == 'OrangeHRM'
        assert_that('OrangeHRM').is_equal_to(actual_title)

    def test_header(self, setup):
        actual_header = self.driver.find_element(By.XPATH, '//h5').text
        assert_that(actual_header).is_equal_to('Login')

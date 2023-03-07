import time

import pytest
from assertpy import assert_that
from selenium import webdriver
from selenium.webdriver.common.by import By

from base.webdriver_listner import WebDriverWrapper


class TestLogin(WebDriverWrapper):
    @pytest.mark.parametrize("username, password", [("Admin", "admin123")])
    def test_valid_login(self, username, password):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        actual_text = self.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text
        assert_that("Dashboard").is_equal_to(actual_text)

    @pytest.mark.parametrize("username, password, cred_error", [
        ("Admin1", "admin1", "Invalid credentials"),
        ("Admin2", "admin2", "Invalid credentials")
    ])
    def test_invalid_login(self, username, password, cred_error):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        actual_error = self.driver.find_element(By.XPATH,
                                                "//p[text()='Invalid credentials']").text
        assert_that(cred_error).is_equal_to(actual_error)


class TestLoginUI(WebDriverWrapper):
    def test_title(self):
        actual_title = self.driver.title
        assert actual_title == 'OrangeHRM'
        assert_that('OrangeHRM').is_equal_to(actual_title)

    def test_header(self):
        actual_header = self.driver.find_element(By.XPATH, '//h5').text
        assert_that(actual_header).is_equal_to('Login')

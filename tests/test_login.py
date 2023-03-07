import time

import pytest
from assertpy import assert_that
from selenium import webdriver
from selenium.webdriver.common.by import By

from base.webdriver_listner import WebDriverWrapper


class TestLogin(WebDriverWrapper):
    def test_valid_login(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        actual_text = self.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text
        assert_that("Dashboard").is_equal_to(actual_text)

    def test_invalid_login(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin1234")
        self.driver.find_element(By.NAME, "password").send_keys("admin1234")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        actual_error = self.driver.find_element(By.XPATH,
                                                "//p[text()='Invalid credentials']").text
        assert_that("Invalid credentials").is_equal_to(actual_error)


class TestLoginUI(WebDriverWrapper):
    def test_title(self):
        actual_title = self.driver.title
        assert actual_title == 'OrangeHRM'
        assert_that('OrangeHRM').is_equal_to(actual_title)

    def test_header(self):
        actual_header = self.driver.find_element(By.XPATH, '//h5').text
        assert_that(actual_header).is_equal_to('Login')

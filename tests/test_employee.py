import time

import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By

from base.webdriver_listner import WebDriverWrapper
from utilities import data_source


class TestEmployee(WebDriverWrapper):
    @pytest.mark.parametrize("username, password", data_source.test_valid_login_data)
    def test_valid_login(self, username, password):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

        self.driver.find_element(By.LINK_TEXT, 'PIM').click()
        self.driver.find_element(By.LINK_TEXT, 'Add Employee').click()
        self.driver.find_element(By.NAME, 'firstName').send_keys('John')
        self.driver.find_element(By.NAME, 'middleName').send_keys('J')
        self.driver.find_element(By.NAME, 'lastName').send_keys('Week')
        self.driver.find_element(By.XPATH, '//button[normalize-space()="Save"]').click()

        time.sleep(3)
        # employee_name = self.driver.find_element(By.XPATH, '//div[@class="orangehrm-edit-employee-name"]/h6').text
        # employee_first_name = self.driver.find_element(By.NAME, 'firstName').text
        # assert_that(employee_name).is_equal_to('John Week')
        # assert_that(employee_first_name).is_equal_to('John')

import time

import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By

from base.webdriver_listner import WebDriverWrapper
from utilities import data_source


class TestEmployee(WebDriverWrapper):
    @pytest.mark.parametrize("username, password, first_name, middle_name, last_name, full_name, verify_f_name",
                             data_source.test_add_employee_data)
    def test_valid_login(self, username, password, first_name, middle_name, last_name, full_name, verify_f_name):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

        self.driver.find_element(By.LINK_TEXT, 'PIM').click()
        self.driver.find_element(By.LINK_TEXT, 'Add Employee').click()
        self.driver.find_element(By.NAME, 'firstName').send_keys(first_name)
        self.driver.find_element(By.NAME, 'middleName').send_keys(middle_name)
        self.driver.find_element(By.NAME, 'lastName').send_keys(last_name)
        self.driver.find_element(By.XPATH, '//button[normalize-space()="Save"]').click()

        time.sleep(3)
        employee_name = self.driver.find_element(By.XPATH,
                                                 f'//h6[contains(normalize-space(),"{first_name}")]').text
        employee_first_name = self.driver.find_element(By.NAME, "firstName").get_attribute("value")
        assert_that(employee_name).is_equal_to(full_name)
        assert_that(employee_first_name).is_equal_to(first_name)

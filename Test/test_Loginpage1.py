import os
import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.select import Select
from Test.takescreenshot import take_screenshot, take_successscreenshot
from Utilities.BaseClass import BaseClass


class Test_Case1(BaseClass):
    def test_loginpage(self):
        wait = WebDriverWait(self.driver, 10)

        try:
            self.driver.find_element(By.NAME, "name").send_keys("pramilamani")
            self.driver.find_element(By.NAME, "email").send_keys("pramilaeceian@gmail.com")
            self.driver.find_element(By.ID, "exampleInputPassword1").send_keys("pramilaeceian@gmail.com")
            time.sleep(2)
            # Wait until the checkbox is present
            drpdown = Select(self.driver.find_element(By.ID, 'exampleFormControlSelect1'))
            drpdown.select_by_visible_text("Female")
            self.driver.find_element(By.XPATH,"//label[normalize-space()='Student']")
            date_picker = wait.until(EC.element_to_be_clickable((By.NAME, 'bday')))
            time.sleep(2)
            date_picker.click()

            # Option 1: Directly entering the date if the input field accepts text input
            date_picker.send_keys('06-01-1991')  # Enter the date in the required format
            date_picker.send_keys(Keys.RETURN)
            #self.driver.find_element(By.XPATH, "//input[value='Submit']")

            screenshot_path = take_successscreenshot(self.driver,"Tests/SucessScreenshots", prefix='success_login')
            print(f"Screenshot saved at {screenshot_path}")


        except Exception as e:
        # Take a screenshot if an error occurs
            screenshot_path = take_screenshot(self.driver,"Tests/ErrorScreenshots", prefix='error_login')
            print(f"An error occurred: {e}")
            print(f"Screenshot saved to {screenshot_path}")
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Test.takescreenshot import take_screenshot
from Utilities.BaseClass import BaseClass

class Test_Case1(BaseClass):
    def test_loginpage(self):
        try:
            self.driver.find_element(By.NAME,"userName").send_keys("pramilamani")
            self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Maylnt@2024")
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//iframe[@title="reCAPTCHA"]'))
            )

            # Switch to the reCAPTCHA iframe
            iframe = self.driver.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]')
            self.driver.switch_to.frame(iframe)

            # Wait until the checkbox is present
            checkbox = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'recaptcha-anchor'))
            )

            # Click the reCAPTCHA checkbox
            checkbox.click()
            self.driver.switch_to.default_content()
            self.driver.find_element(By.CLASS_NAME,"btn-primary").click()

        except Exception as e:
        # Take a screenshot if an error occurs
            screenshot_path = take_screenshot(self.driver, prefix='error')
            print(f"An error occurred: {e}")
            print(f"Screenshot saved to {screenshot_path}")
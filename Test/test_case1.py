import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.BaseClass import BaseClass

class Test_Case1(BaseClass):

    def test_openbrowser(self):
        self.driver.find_element(By.ID,"ra_userName").send_keys("mani")

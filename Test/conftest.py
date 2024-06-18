import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://tenncareconnect.tn.gov/register-account")
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()

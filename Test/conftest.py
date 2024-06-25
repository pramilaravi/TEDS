import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome" , help="Browser name to use for testing: chrome, firefox, ie"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    logger.info(f"Selected browser: {browser_name}")

    if browser_name == "chrome":
        driver = webdriver.Chrome()
        logger.info("Chrome browser started")
        """ chrome_options = ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)"""
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
        logger.info("Firefox browser started")
        """firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--start-maximized")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)"""
    elif browser_name == "ie":
        driver = webdriver.Ie(IEDriverManager().install())
        logger.info("Internet Explorer browser started")
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    ##driver.get("https://tenncareconnect.tn.gov/signin")
    driver.get("https://rahulshettyacademy.com/angularpractice")
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()

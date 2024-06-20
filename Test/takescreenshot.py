import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def take_screenshot(driver, base_dir='Tests/Screenshots', prefix='screenshot'):
    """
    Takes a screenshot of the current browser window and saves it to the specified directory.

    :param driver: The WebDriver instance.
    :param base_dir: The base directory where screenshots will be saved.
    :param prefix: The prefix for the screenshot file name.
    :return: The path to the saved screenshot.
    """
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    file_name = f"{prefix}_{timestamp}.png"
    file_path = os.path.join(base_dir, file_name)
    driver.save_screenshot(file_path)
    return file_path

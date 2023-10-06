from Scripts.selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest

# Define Chrome options
chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])


@pytest.fixture()
def driver():
    print("Creating chrome driver")
    # Use the defined chrome_options when creating the webdriver
    my_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    yield my_driver
    print("Closing chrome driver")
    my_driver.quit()

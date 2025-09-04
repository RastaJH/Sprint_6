import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions

@pytest.fixture(scope="session")
def base_url():
    return "https://qa-scooter.praktikum-services.ru/"

@pytest.fixture
def driver():
    options = FirefoxOptions()
    options.add_argument("--width=1400")
    options.add_argument("--height=1000")
    
    service = FirefoxService()
    driver = webdriver.Firefox(service=service, options=options)
    driver.implicitly_wait(10)
    
    yield driver
    driver.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--width=1400")
    options.add_argument("--height=1000")
    
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(10)
    
    yield driver
    driver.quit()
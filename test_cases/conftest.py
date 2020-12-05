from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--window-size=1420,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver

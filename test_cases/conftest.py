from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    if browser == 'firefox':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(pasrer):
    pasrer.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

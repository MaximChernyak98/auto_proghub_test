from selenium import webdriver
import pytest
import platform
import msedge-selenium-tools


def pytest_addoption(parser):
    parser.addoption("--browser", default='chrome')


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def browser_with_options(browser):
    if browser == 'firefox':
        browser_options = webdriver.FirefoxOptions()
    # elif browser == 'edge' TODO https://stackoverflow.com/questions/62951105/how-to-set-options-for-chromium-edge-in-selenium
    #     browser_options = webdriver.EdgeOp
    else:
        browser_options = webdriver.ChromeOptions()

    browser_options.add_argument('--no-sandbox')
    browser_options.add_argument('--window-size=1420,1080')
    browser_options.add_argument('--headless')
    browser_options.add_argument('--disable-gpu')

    if browser == 'firefox':
        driver = webdriver.Firefox(firefox_options=browser_options)
    # elif browser == 'edge':
    #     driver = webdriver.Edge
    else:
        driver = webdriver.Chrome(chrome_options=browser_options)


@pytest.fixture()
def setup(browser):
    driver = None
    if platform.system() == 'Windows':
        if browser == 'firefox':
            driver = webdriver.Firefox()
            print("Launching Firefox Browser")
        else:
            driver = webdriver.Chrome()
            print("Launching Chrome Browser")
    else:
        driver = browser_with_options(browser)
    return driver

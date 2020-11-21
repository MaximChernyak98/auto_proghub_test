from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import os
import time


class ProgHubParser():
    def __init__(self, driver, type_of_test):
        self.driver = driver
        self.type_of_test = type_of_test

    def go_to_tests_page(self):
        self.driver.get("https://proghub.ru/tests")

    def parse(self):
        self.go_to_tests_page()
        test_cards = self.driver.find_elements_by_css_selector('div[class="testCard"]>a')
        for test in test_cards:
            link = test.get_attribute("href")
            print(link)


def start_driver():
    current_dir = os.getcwd()
    paths_to_webdriver = os.path.join(current_dir, 'chromedriver.exe')
    driver = webdriver.Chrome(executable_path=paths_to_webdriver)
    driver.set_window_position(1000, 0)
    return driver


def main():
    driver = start_driver()
    parser = ProgHubParser(driver, 'a')
    parser.parse()


if __name__ == "__main__":
    main()


# try:
#         button = driver.find_element_by_class_name("btn-primary")
#         button.click()
#         time.sleep(3)
#     except NoSuchElementException:
#         print("Не нашел данный элемент")

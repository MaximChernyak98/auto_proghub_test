# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


import os
import time
import logging


test_logger = logging.getLogger()
test_logger.setLevel(logging.INFO)  # or whatever
handler = logging.FileHandler('yandex_tester.log', 'w', 'utf-8')  # or whatever
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))  # or whatever
test_logger.addHandler(handler)


class YandexTester():
    def __init__(self, driver, test_page):
        self.driver = driver
        self.test_page = test_page

    def go_to_test_page(self):
        self.driver.get(self.test_page)

    def check_search_box_load(self, delay):
        try:
            type_of_search = (By.ID, 'text')
            self.search_box = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located(type_of_search))
            test_logger.info("Поле поиска найдено по ID = text")
        except TimeoutException:
            self.search_box = None
            test_logger.error(f"Поле поиска не найдено за {delay} секунд")

    def check_suggest_box_load(self, delay):
        self.search_box.send_keys("Тензор")
        time.sleep(1)
        suggest_box = self.driver.find_element_by_class_name('input_ahead-visible_yes')
        if suggest_box:
            test_logger.info("Таблица с подсказками найдена")
        else:
            test_logger.error("Таблица с подсказками не найдена")

    def check_results_load(self, delay):
        self.search_box.send_keys("Тензор")
        self.search_box.send_keys(Keys.RETURN)
        try:
            type_of_search = (By.CLASS_NAME, "serp-item")
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located(type_of_search))
            self.request_results = self.driver.find_elements_by_class_name("serp-item")
            for element in self.request_results:
                a = element.find_element_by_tag_name('a')
                print(a.get_attribute("href"))

            if self.request_results:
                test_logger.info("Получены результаты по запросу")
            else:
                test_logger.error("Поле с результатами по классу serp-item не найдены")
        except TimeoutException:
            test_logger.error(f"Поле поиска не найдено за {delay} секунд")

    def find_link_in_request_results(self):
        for result in self.request_results:
            print(result.get_attribute("href"))


def start_driver():
    current_dir = os.getcwd()
    paths_to_webdriver = os.path.join(current_dir, 'chromedriver.exe')
    try:
        driver = webdriver.Chrome(executable_path=paths_to_webdriver)
        driver.set_window_position(960, 0)
        test_logger.info("Драйвер запущен успешно")
        return driver
    except FileExistsError:
        test_logger.info("Не найден chromedriver.exe")


def main():
    test_logger.info("Начало теста")
    driver = start_driver()
    yandex_tester = YandexTester(driver, test_page="https://yandex.ru/")
    yandex_tester.go_to_test_page()
    yandex_tester.check_search_box_load(3)
    yandex_tester.check_suggest_box_load(3)
    yandex_tester.check_results_load(3)
    # yandex_tester.find_link_in_request_results()
    time.sleep(5)
    # parser.parse()


if __name__ == "__main__":
    main()

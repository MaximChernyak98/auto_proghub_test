import pytest
from selenium import webdriver
from page_objects.login_page import LoginPage
from utilities.read_properties import ReadConfig


class Test_001_Login:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    def test_home_page_title(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        self.driver.close()
        if actual_title == "Your store. Login":
            assert True
        else:
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_user_name(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login_button()
        actual_title = self.driver.title
        self.driver.close()
        if actual_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False

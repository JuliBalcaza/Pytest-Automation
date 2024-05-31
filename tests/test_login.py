import pytest
from selenium import webdriver
from POM.base_page import BasePage
from POM.login_page import LoginPage
from helpers.credentials import USER, PASSWORD


class TestLogin:
    def setup_method(self):
        self.base_page = BasePage(webdriver)  # Crear una instancia de BasePage
        self.base_page.setup_method()

    @pytest.mark.parametrize('username, password', [(USER, PASSWORD)])
    def test_login(self, username, password):
        login_page = LoginPage(self.base_page.driver)  # Crear una instancia de LoginPage
        login_page.set_username(username)  # Usar el método set_username de LoginPage
        login_page.set_password(password)  # Usar el método set_password de LoginPage
        login_page.click_login()  # Usar el método click_login de LoginPage

        expected_url = 'https://www.saucedemo.com/inventory.html'
        current_url = self.base_page.driver.current_url  # Obtener la URL actual del navegador

        assert expected_url == current_url, f'Error. Expected URL {expected_url}, but current URL: {current_url}'

    def teardown_method(self):
        self.base_page.driver.quit()

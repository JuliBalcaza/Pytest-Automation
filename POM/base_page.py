from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def wait_for_element(self, timeout, *locator):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def setup_method(self):
        service = Service(executable_path=r'/Users/julietabalcaza/PycharmProjects/test_wizeline/chromedriver')
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(5)
        self.driver.get('https://www.saucedemo.com/')

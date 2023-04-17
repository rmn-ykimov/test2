from selenium import webdriver

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager


class WebDriverFactory:
    def __init__(self, browser):
        self.browser = browser

    def create_driver(self):
        if self.browser == "firefox":
            service = FirefoxService(
                executable_path=GeckoDriverManager().install())
            return webdriver.Firefox(service=service)
        elif self.browser == "chrome":
            service = ChromeService(
                executable_path=ChromeDriverManager().install())
            return webdriver.Chrome(service=service)
        else:
            raise ValueError("Неверный браузер")


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Logout:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    ACCOUNT_BUTTON = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/nav/div/div[2]/button')

    LOGOUT_BUTTON = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/nav/div/div[2]/ul/li[2]/button')

    LOGIN_PAGE_ELEMENT = (By.XPATH, '//*[@id="app"]/div/div/div[1]/div[1]/form/div/div[3]/button')


    def click_account_button(self):
        account_button = self.wait.until(EC.element_to_be_clickable(self.ACCOUNT_BUTTON))
        account_button.click()

    def click_logout_button(self):
        logout_button = self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BUTTON))
        logout_button.click()

    def moving_to_login_page(self, driver):
        _ = self.wait.until(EC.visibility_of_element_located(self.LOGIN_PAGE_ELEMENT))
        assert driver.current_url == 'https://portal.servers.com/login', 'User was not redirected to the login page'


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    COOKIES_BUTTON = (By.XPATH, '//*[@id="CybotCookiebotDialogBodyButtonDecline"]')

    EMAIL_INPUT = (By.XPATH, '//*[@id="app"]/div/div/div[1]/div[1]/form/div/div[1]/div/input')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="app"]/div/div/div[1]/div[1]/form/div/div[2]/div/input')
    LOGIN_BUTTON = (By.CLASS_NAME, 'sv8lcon')

    DASHBOARD_ELEMENT = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/nav/div/div[2]/button')


    def click_cookies_button(self):
        cookies_button = self.wait.until(EC.element_to_be_clickable(self.COOKIES_BUTTON))
        cookies_button.click()

    def enter_email(self, EMAIL):
        email_field = self.wait.until(EC.presence_of_element_located(self.EMAIL_INPUT))
        email_field.send_keys(EMAIL)

    def enter_password(self, PASSWORD):
        password_field = self.wait.until(EC.presence_of_element_located(self.PASSWORD_INPUT))
        password_field.send_keys(PASSWORD)

    def click_login_button(self):
        login_button = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        login_button.click()

    def moving_to_dashboard(self, driver):
        _ = self.wait.until(EC.visibility_of_element_located(self.DASHBOARD_ELEMENT))
        assert driver.current_url == 'https://portal.servers.com/dashboard', 'User was not redirected to the dashboard'


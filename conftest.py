import pytest
from factory import WebDriverFactory
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from page_object.login_page import LoginPage
from configuration import URL, EMAIL, PASSWORD


@pytest.fixture()
def driver():
    factory = WebDriverFactory("firefox")
    driver = factory.create_driver()
    yield driver
    driver.quit()

@pytest.fixture()
def login(driver):

    driver.get(URL)

    login_page = LoginPage(driver)

    login_page.click_cookies_button()

    login_page.enter_email(EMAIL)

    login_page.enter_password(PASSWORD)

    login_page.click_login_button()

    login_page.moving_to_dashboard(driver)

    return driver


@pytest.fixture()
def logout(login):

    driver = login

    wait = WebDriverWait(driver, 10)

    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/nav/div/div[2]/button')))
    button.click()

    logout_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/nav/div/div[2]/ul/li[2]/button')))
    logout_button.click()

    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[1]/div[1]/form/div/div[3]/button')))
    assert driver.current_url == 'https://portal.servers.com/login', 'User was not redirected to the login page'


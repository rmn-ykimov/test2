from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from configuration import STREET, EMAIL, FIRST_NAME, LAST_NAME, PHONE_NUMBER, CITY, POSTAL_CODE, REGION


def test_filling_account_info(login):

    driver = login

    wait = WebDriverWait(driver, 10)

    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/nav/div/div[2]/button')))
    button.click()

    profile = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/nav/div/div[2]/ul/li[1]/a')))
    profile.click()

    edit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div/div[1]/div/button')))
    edit_button.click()

    account_type_rb = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="business_type"]/div[2]/label[1]/span/input')))
    account_type_rb.click()

    currency_type_rb = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="currency"]/div[2]/label[1]/span/input')))
    currency_type_rb.click()

    first_name_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div/form/div[4]/div[1]/div[2]/div[1]/div[1]/div/div/div/div/input')))
    first_name_field.send_keys(FIRST_NAME)

    last_name_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div/form/div[4]/div[1]/div[2]/div[1]/div[2]/div/div/div/div/input')))
    last_name_field.send_keys(LAST_NAME)

    phone_number_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div/form/div[4]/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/div/input')))
    phone_number_field.send_keys(PHONE_NUMBER)

    email_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div/form/div[4]/div[1]/div[2]/div[2]/div[2]/div/div/div/div/input')))
    email_field.send_keys(EMAIL)

    coutry_field = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div/form/div[5]/div[1]/div[2]/div[1]/div[1]/div/div/div/div/div/div[1]')
    driver.execute_script("arguments[0].scrollIntoView();", coutry_field)
    coutry_field.click()

    country = driver.find_element(By.XPATH, '//*[@id="react-select-2-option-195"]/div/div')
    country.click()

    city_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div/form/div[5]/div[1]/div[2]/div[1]/div[2]/div/div/div/div/input')))
    city_field.send_keys(CITY)

    postal_code_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div/form/div[5]/div[1]/div[2]/div[2]/div[2]/div/div/div/div/input')))
    postal_code_field.send_keys(POSTAL_CODE)

    region_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div/form/div[5]/div[1]/div[2]/div[2]/div[1]/div/div/div/div/input')))
    region_field.send_keys(REGION)

    street_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div/form/div[5]/div[1]/div[2]/div[3]/div/div/div/div/div/input')))
    street_field.send_keys(STREET)

    save_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div/form/footer/div[2]/div[1]/button[2]')))
    save_button.click()


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from configuration import SERVER_NAME


def test_cloud_server_order(login):

    driver = login

    wait = WebDriverWait(driver, 10)

    cloud_server_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[1]/ul/li[2]/span')))
    cloud_server_field.click()

    create_and_manage_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[1]/ul/li[2]/ul/li[1]/a')))
    create_and_manage_field.click()

    create_server_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div[1]/div/a[2]')))
    create_server_button.click()

    location_rb = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="location_id"]/div[2]/label[1]/span/input')))
    location_rb.click()

    image_rb = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div/form/div[2]/div[1]/div[2]/label[8]/span/input')))
    driver.execute_script("arguments[0].scrollIntoView();", image_rb)
    image_rb.click()

    configuration_rb = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="flavor_id"]/div[2]/label[1]/span/input')))
    driver.execute_script("arguments[0].scrollIntoView();", configuration_rb)
    configuration_rb.click()

    ssh_checkbox = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="auth_methods"]/div[2]/label[1]/span/input')))
    driver.execute_script("arguments[0].scrollIntoView();", ssh_checkbox)

    generate_ssh_key_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ssh_key_fingerprint"]/div[1]/div/button[2]')))
    driver.execute_script("arguments[0].scrollIntoView();", generate_ssh_key_button)
    generate_ssh_key_button.click()

    backup_rb = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="backup_enabled"]/div[2]/label[2]/span/input')))
    driver.execute_script("arguments[0].scrollIntoView();", backup_rb)
    backup_rb.click()

    ipv6_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div/form/div[5]/div[1]/div[2]/label/span/input')))
    driver.execute_script("arguments[0].scrollIntoView();", ipv6_checkbox)
    ipv6_checkbox.click()

    cloud_server_name_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="name"]/div[2]/div/div/input')))
    driver.execute_script("arguments[0].scrollIntoView();", cloud_server_name_field)
    cloud_server_name_field.send_keys(SERVER_NAME)

    create_cloud_server_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div/form/footer/div[2]/div[1]/button')))
    driver.execute_script("arguments[0].scrollIntoView();", create_cloud_server_button)
    create_cloud_server_button.click()

    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div/div/button[1]')))
    assert driver.current_url == 'https://portal.servers.com/payment/methods', 'User was not redirected to the payment page'


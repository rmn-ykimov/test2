import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


def test_dedicated_servers(login):

    driver = login

    wait = WebDriverWait(driver, 10)

    dedicated_servers_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[1]/ul/li[1]/span')))
    dedicated_servers_field.click()

    manage_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[1]/ul/li[1]/ul/li[1]/a')))
    manage_field.click()

    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div[1]/div/div/div/input')))
    assert driver.current_url == 'https://portal.servers.com/servers/my', 'User was not redirected to the servers page'


def test_cloud_storage(login):

    driver = login

    wait = WebDriverWait(driver, 10)

    cloud_storage_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[1]/ul/li[3]/a')))
    cloud_storage_field.click()

    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/a[2]')))
    assert driver.current_url == 'https://portal.servers.com/cloud-storage/0/info', 'User was not redirected to the cloud storage page'


def test_dns(login):

    driver = login

    wait = WebDriverWait(driver, 10)

    dns_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[1]/ul/li[4]/a')))
    dns_field.click()

    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div[1]/div/a')))
    assert driver.current_url == 'https://portal.servers.com/dns', 'User was not redirected to the cloud DNS page'


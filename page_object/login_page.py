# from selenium import webdriver
#
#
# class LoginPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.url = "https://www.example.com/login"
#         self.username_textbox_id = "username"
#         self.password_textbox_id = "password"
#         self.login_button_id = "loginBtn"
#
#     def navigate(self):
#         self.driver.get(self.url)
#
#     def enter_username(self, username):
#         self.driver.find_element_by_id(self.username_textbox_id).clear()
#         self.driver.find_element_by_id(self.username_textbox_id).send_keys(
#             username)
#
#     def enter_password(self, password):
#         self.driver.find_element_by_id(self.password_textbox_id).clear()
#         self.driver.find_element_by_id(self.password_textbox_id).send_keys(
#             password)
#
#     def click_login(self):
#         self.driver.find_element_by_id(self.login_button_id).click()
#
#
# driver = webdriver.Chrome()
# login_page = LoginPage(driver)
# login_page.navigate()
# login_page.enter_username("testuser")
# login_page.enter_password("testpassword")
# login_page.click_login()

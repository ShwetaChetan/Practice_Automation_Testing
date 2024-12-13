from selenium.webdriver.common.by import By


class Login:

    def __init__(self, driver):
        self.driver = driver
        self.textbox_username = (By.ID, "uname")
        self.textbox_password = (By.ID, "pwd")
        self.button_login = (By.XPATH, "//input[@type='submit']")

    def open_page(self, url):
        self.driver.get(url)

    def set_username(self, user):
        self.driver.find_element(*self.textbox_username).send_keys(user)

    def set_password(self, password):
        self.driver.find_element(*self.textbox_password).send_keys(password)

    def set_login(self):
        self.driver.find_element(*self.button_login).click()

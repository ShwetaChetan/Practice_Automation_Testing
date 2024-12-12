from selenium.webdriver.common.by import By


class Login():

  def __init__(self,driver):
    self.driver = driver
    self.textbox_email = (By.ID,"Email")
    self.textbox_password = (By.ID,"Password")
    self.checkbox_remember = (By.ID,"RememberMe")
    self.click_login = (By.XPATH,"//button[normalize-space()='Log in']")

  def set_email(self,email):
      email_field = self.driver.find_element(*self.textbox_email)
      email_field.clear()
      email_field.send_keys(email)

  def set_password(self,password):
      password_field = self.driver.find_element(*self.textbox_password)
      password_field.clear()
      password_field.send_keys(password)


 # def set_remember(self,remember):
  #    self.driver.find_element(*self.checkbox_remember)
  #    if checkbox.is_selected() != remember:
 #         checkbox.click()

  def set_login(self):
      self.driver.find_element(*self.click_login).click()

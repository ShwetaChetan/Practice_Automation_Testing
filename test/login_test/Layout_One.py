from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By




class Layout:

    def __init__(self, driver):
        self.driver = driver
        self.test_alert_button = (By.XPATH, "//button[normalize-space()='Your Sample Alert Button!']")
        self.click_sample_button = (By.XPATH, "//button[normalize-space()='Double-click me']")
        self.select_source_element = (By.ID, "div1")
        self.select_target_element = (By.ID, "drag1")

    def open_page1(self, url):
        self.driver.get(url)

    def set_alert_button(self):
        self.driver.find_element(*self.test_alert_button).click()


    def set_sample_doubleclick(self):
        element = self.driver.find_element(*self.click_sample_button)
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()

    def set_sample_drag_drop(self):
        source_element = self.driver.find_element(*self.select_source_element)
        target_element = self.driver.find_element(*self.select_target_element)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()








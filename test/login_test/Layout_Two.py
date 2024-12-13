
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class LayoutTwo:
    def __init__(self, driver):
        self.driver = driver
        self.textbox_firstname = (By.ID, "fname")
        self.textbox_lastname = (By.ID, "lname")
        self.button_gender = (By.ID, "female")
        self.option_dropdown = (By.ID, "option")
        self.click_checkbox = (By.NAME, "option3")
        self.write_typing_answer = (By.CSS_SELECTOR, "input[name='Options']")
        self.list_element = (By.ID, "//datalist[@id='datalists']//option")
        self.select_color = (By.ID, "favcolor")
        self.scroll_select = (By.XPATH, "//input[@id='a']")
        self.click_choose_file = (By.XPATH, "//input[@id='myfile']")

    def open_page2(self, url):
        self.driver.get(url)

    def set_firstname(self, firstname):
        self.driver.find_element(*self.textbox_firstname).send_keys(firstname)

    def set_lastname(self, lastname):
        self.driver.find_element(*self.textbox_lastname).send_keys(lastname)

    def set_gender(self):
        self.driver.find_element(*self.button_gender).click()

    def set_dropdown(self):
        element = self.driver.find_element(*self.option_dropdown)
        dropdown = Select(element)
        dropdown.select_by_visible_text('Option 2')
        print(len(dropdown.options))
        all_options = dropdown.options

        for option in all_options:
            print(option.text)

    def set_checkbox(self):
        self.driver.find_element(*self.click_checkbox).click()

    def set_typing_answer(self):
        self.driver.find_element(*self.write_typing_answer).send_keys('C')
        self.driver.find_element(*self.write_typing_answer).click()

        list_elements = self.driver.find_elements(*self.list_element)

        print(len(list_elements))

        for element in list_elements:
            print(element.text)

    def set_favorite_color(self):
        self.driver.find_element(*self.select_color).click()

    def set_scroll_range(self):
        scroll = self.driver.find_element(*self.scroll_select)
        #self.driver.execute_script("return arguments[0].scrollIntoView(true);", scroll)
        



    def set_select_choose_file(self):
        self.driver.find_element(*self.click_choose_file).send_keys("C://Users/USER/Pictures/Saved Pictures/world.jpg")

import time
import unittest
import HtmlTestRunner
from selenium import webdriver
import sys

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


sys.path.append("/")
from page_objects.login_page import Login

class LoginTest(unittest.TestCase):
    baseURL = "http://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        lp = Login(self.driver)
        lp.set_email(self.username)
        lp.set_password(self.password)
        lp.set_login()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__=='__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..//reports'))






import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from test.page_object.Login_page import Login
from test.login_test.Layout_One import Layout
from test.login_test.Layout_Two import LayoutTwo


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def testcase1_login(driver):
    lp = Login(driver)
    lp.open_page("https://trytestingthis.netlify.app/")
    time.sleep(3)
    lp.set_username("test")
    time.sleep(3)
    lp.set_password("test")
    time.sleep(3)
    lp.set_login()
    time.sleep(5)


def test_alert_button(driver):
    lo = Layout(driver)
    lo.open_page1("https://trytestingthis.netlify.app/")
    time.sleep(3)
    lo.set_alert_button()
    time.sleep(3)


def test_doubleclick_operation(driver):
    lo = Layout(driver)
    lo.open_page1("https://trytestingthis.netlify.app/")
    time.sleep(3)
    driver.maximize_window()
    lo.set_sample_doubleclick()
    time.sleep(10)


def test_drag_and_drop(driver):
    dd = Layout(driver)
    dd.open_page1("https://trytestingthis.netlify.app/")
    time.sleep(3)
    driver.maximize_window()
    dd.set_sample_drag_drop()
    time.sleep(10)


def test_first_name(driver):
    fn = LayoutTwo(driver)
    fn.open_page2("https://trytestingthis.netlify.app/")
    time.sleep(3)
    driver.maximize_window()
    fn.set_firstname("Text")
    fn.set_lastname("Text")
    time.sleep(5)


def test_gender(driver):
    tg = LayoutTwo(driver)
    tg.open_page2("https://trytestingthis.netlify.app/")
    time.sleep(3)
    tg.set_gender()
    time.sleep(5)


def test_dropdown(driver):
    td = LayoutTwo(driver)
    td.open_page2("https://trytestingthis.netlify.app")
    time.sleep(3)
    td.set_dropdown()
    time.sleep(5)


def test_checkbox(driver):
    tc = LayoutTwo(driver)
    tc.open_page2("https://trytestingthis.netlify.app")
    time.sleep(3)
    tc.set_checkbox()
    time.sleep(5)
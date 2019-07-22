from selenium import webdriver
import pytest
def test_selenium():
    #geckodriver = r'C:\Users\mohit.agarwal\PycharmProjects\Practice\Driver'
    options = webdriver.FirefoxOptions()
    #options.add_argument('-headless')
    browser = webdriver.Firefox(firefox_options=options)
    browser.get('http://www.google.com')
    assert browser.title=="Google"
    browser.quit()
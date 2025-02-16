from selenium import webdriver
from config import BROWSER

def get_driver():
    if BROWSER == "chrome":
        return webdriver.Chrome()
    elif BROWSER == "firefox":
        return webdriver.Firefox()
    elif BROWSER == "edge":
        return webdriver.Edge()
    elif BROWSER == "safari":
        return webdriver.Safari()
    else:
        raise ValueError("Unknown browser")
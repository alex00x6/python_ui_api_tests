import platform
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

winprefix = "../../resources/selenium/windows/"
linuxprefix = "../../resources/selenium/linux/"


def createinstance(browsername):
    global driver
    if platform.system() == 'Windows':
        if browsername == 'chrome':
            driver = webdriver.Chrome(winprefix + "chromedriver.exe")
        if browsername == 'firefox':
            driver = webdriver.Firefox(winprefix + "geckodriver32.exe")

    if platform.system() == "Linux":
        print("LINUX IS NOT SUPPORTED YET!")

    if driver is not None:
        driver.implicitly_wait(50)
        driver.maximize_window()
        return driver


def waitforjs(driver):
    counter = 0
    while not driver.execute_script("return document.readyState").__eq__("complete") & counter < 20:
        print("JS not ready yet")
        sleep(0.1)


def waitforclickableByXpath(driver, xpath):
    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, xpath)))


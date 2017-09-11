from selenium import webdriver
import platform
import os
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait

winprefix = "../../resources/selenium/windows/"
linuxprefix = "../../resources/selenium/linux/"


def createinstance(browsername):
    global driver
    if platform.system() == 'Windows':
        if browsername == 'chrome':
            driver = webdriver.Chrome(executable_path=winprefix+"chromedriver.exe")
        if browsername == 'firefox':
            driver = webdriver.Firefox(executable_path=winprefix+"geckodriver32.exe")

    if platform.system() == "Linux":
        print("LINUX BLYA, IS NOT SUPPORTED YET!")

    if driver is not None:
        driver.implicitly_wait(50)
        driver.maximize_window()
        return driver


def waitforjs(driver):
    counter = 0
    while not driver.execute_script("return document.readyState").__eq__("complete") & counter < 20:
        print("JS not ready yet")
        sleep(0.1)

def waitforclickable(driver):
    WebDriverWait(driver, 15).

driver = createinstance("chrome")

driver.get("http://google.com")
driver.find_element_by_xpath("//input[@aria-label=\"Найти\"]").send_keys("smth")
waitforjs(driver)
waitforclickable()
driver.find_element_by_xpath("//*[@value=\"Поиск в Google\"]").click()
sleep(5)
driver.quit()

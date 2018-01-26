from src.driver.WebDriverHelper import *

driver = createinstance("chrome")

driver.get("http://google.com")
driver.find_element_by_xpath("//input[@aria-label=\"Найти\"]").send_keys("smth")
waitforjs(driver)
waitforclickableByXpath(driver, "//*[@value=\"Поиск в Google\"]")
driver.find_element_by_xpath("//*[@value=\"Поиск в Google\"]").click()
assert len(driver.find_elements_by_xpath("//div[@id='search']//*[contains(text(), 'smth')]")) > 0
driver.quit()

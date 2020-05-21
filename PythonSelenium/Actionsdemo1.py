import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\\abhkhane\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
time.sleep(5)
Action = ActionChains(driver)

Action.context_click(driver.find_element_by_xpath("//div/input[@id='double-click']")).perform()
Action.double_click(driver.find_element_by_xpath("//div/input[@id='double-click']")).perform()

alert=driver.switch_to.alert
alert.accept()
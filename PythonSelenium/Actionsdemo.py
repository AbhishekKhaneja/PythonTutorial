import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\\abhkhane\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.familysearch.org/en/")
driver.maximize_window()
time.sleep(5)
driver.find_element_by_xpath("//div[@class='primary-nav-item nav-menu-parent '][2]").click()
Action = ActionChains(driver)
Action.move_to_element(driver.find_element_by_link_text("Catalog")).click().perform()

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
time.sleep(5)
Action.double_click(driver.find_element_by_xpath("//div/input[@id='double-click']")).perform()


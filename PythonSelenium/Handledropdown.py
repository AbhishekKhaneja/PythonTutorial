from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\abhkhane\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")

#creating the object of a Select class
dropDown=Select(driver.find_element_by_xpath("//select[@id='exampleFormControlSelect1']"))
dropDown.select_by_visible_text("Female")
dropDown.select_by_index(0)

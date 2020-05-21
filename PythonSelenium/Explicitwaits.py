import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Users\\abhkhane\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
count=len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
Count=driver.find_elements_by_xpath("//div[@class='product-action']/button")
for j in Count:
    j.click()
driver.find_element_by_xpath("//img[@src='./images/bag.png']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait=WebDriverWait(driver,6)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='promoInfo']")))
print(driver.find_element_by_xpath("//span[@class='promoInfo']").text)

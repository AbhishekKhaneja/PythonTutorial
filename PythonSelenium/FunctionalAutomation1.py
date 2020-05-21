import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Users\\abhkhane\\Downloads\\chromedriver_win32\\chromedriver.exe")
list= []
list2= []
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
#listofproductsfetched=driver.find_elements_by_xpath("//h4[@class='product-name']")

count=len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
Count=driver.find_elements_by_xpath("//div[@class='product-action']/button")
for everybutton in Count:
    list.append(everybutton.find_element_by_xpath("parent::div/parent::div/h4").text)
    everybutton.click()
driver.find_element_by_xpath("//img[@src='./images/bag.png']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
listofproductsfetched1=driver.find_elements_by_xpath("//p[@class='product-name']")
print(len(listofproductsfetched1))
for vegetables in listofproductsfetched1:
    list2.append(vegetables.text)
print(list)
print(list2)
#assert list2 == list

time.sleep(5)
wait=WebDriverWait(driver,6)
AmountbeforecouponApplied=driver.find_element_by_xpath("//b[text()='Total After Discount : ']/following::span").text
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='promoInfo']")))
print(driver.find_element_by_xpath("//span[@class='promoInfo']").text)
AmountaftercouponApplied=driver.find_element_by_css_selector(".discountAmt").text

assert int(AmountbeforecouponApplied) > float(AmountaftercouponApplied)

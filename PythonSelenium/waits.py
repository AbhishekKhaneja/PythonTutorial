import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\abhkhane\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5) # wait until 5 sec if object is not displayed # also name as Global wait
# but since if any page/object displayes in 1.5 second it will resume the execution from there it will not wait all the 5 seconds
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
count=len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
Count=driver.find_elements_by_xpath("//div[@class='product-action']/button")
for j in Count:
    j.click()
driver.find_element_by_xpath("//img[@src='./images/bag.png']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()
print(driver.find_element_by_xpath("//span[@class='promoInfo']").text)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Users\\abhkhane\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_xpath("//a[@href='/angularpractice/shop']").click()
Allproducts=driver.find_elements_by_xpath("//div[@class='card h-100']")
for product in Allproducts:
    product.find_element_by_xpath("div/h4").text
    if product.find_element_by_xpath("div/h4").text == "Blackberry":
        product.find_element_by_xpath("div/button").click()

driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()
driver.find_element_by_css_selector("button[class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("ind")


wait=WebDriverWait(driver,6)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()

assert driver.find_element_by_xpath("//input[@id='checkbox2']").is_selected()

driver.find_element_by_xpath("//input[@class='btn btn-success btn-lg']").click()
SuccessMessage=driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text

print(SuccessMessage)
assert "Success" in SuccessMessage

driver.get_screenshot_as_file("Screen.PNG")



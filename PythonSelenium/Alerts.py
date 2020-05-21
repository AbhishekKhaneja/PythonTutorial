from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\abhkhane\\Downloads\\chromedriver_win32\\chromedriver.exe")
validatetext ="Abhishek"
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_css_selector("input[id='name']").send_keys(validatetext)
driver.find_element_by_id("alertbtn").click()
alert=driver.switch_to.alert
assert(validatetext in alert.text)

print(alert.text)
alert.accept()


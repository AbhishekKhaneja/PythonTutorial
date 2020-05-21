from selenium import webdriver
#browser exposes an executable file
#through selenium test we need to invoke the executable file while will invoke the actual browser
driver = webdriver.Chrome(executable_path="C:\\Users\\abhkhane\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/#/part-time-jobs")
print(driver.title)
print(driver.current_url)
driver.find_element_by_css_selector("input[name='username']").send_keys("Rahul")#using CSS selector
driver.find_element_by_xpath("//input[@name='username']").send_keys("Abhishek") #using xpath


#driver.back()
#driver.minimize_window()
#driver.close()
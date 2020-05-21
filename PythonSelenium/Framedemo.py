from selenium import webdriver



driver = webdriver.Chrome(executable_path="C:\\Users\\abhkhane\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_class_name("mce-content-body ").clear()
driver.find_element_by_class_name("mce-content-body ").send_keys("I am a Automation Tester")
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)
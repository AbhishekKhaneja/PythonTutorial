from selenium import webdriver



driver = webdriver.Chrome(executable_path="C:\\Users\\abhkhane\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element_by_link_text("Click Here").click()
Childwindow=driver.window_handles[1] #0 will denote the parent window #1will denote the childwindow which is opened
driver.switch_to.window(Childwindow)
print(driver.find_element_by_tag_name("h3").text)
driver.close()

driver.switch_to.window(driver.window_handles[0])
print(driver.find_element_by_tag_name("h3").text)

assert "Opening a new window" == driver.find_element_by_tag_name("h3").text

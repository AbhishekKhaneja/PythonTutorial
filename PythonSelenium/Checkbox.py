from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\abhkhane\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

CheckBoxes=driver.find_elements_by_xpath("//input[@type='checkbox']")

#our req. is to click on option2 from the list of chcek box
for i in CheckBoxes:
    if i.get_attribute("value") == "option2":
        i.click()
        assert i.is_selected() # to check if the checkbox is selected or not

radiobuttons = driver.find_elements_by_name("radioButton")
radiobuttons[1].click()
assert(radiobuttons[1].is_selected())


assert driver.find_element_by_id("displayed-text").is_displayed()

driver.find_element_by_id("hide-textbox").click()
assert not driver.find_element_by_id("displayed-text").is_displayed()

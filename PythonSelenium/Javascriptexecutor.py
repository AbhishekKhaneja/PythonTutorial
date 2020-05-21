# javascript DOM can access any elements on webpage just like how selenium does
#selenium have a method to execute javascript code in it

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\abhkhane\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("Abhishek")
print(driver.find_element_by_name("name").text) # it will not print beacuse the value is being passed by selenium through its script in the previous step
print(driver.find_element_by_name("name").get_attribute("value")) #getattribute is the inherited method in selenium form java script document onject model(DOM)

print(driver.execute_script('return document.getElementsByName("name")[0].value')) # here javascript executor comes into picture as driver of selenium is giving control to javascript executor to get the value of the name

#click operation using javascript executor
#using Normal selenium
Shopbutton=driver.find_element_by_xpath("//a[@href='/angularpractice/shop']")

#using Javascript executor
driver.execute_script("arguments[0].click();",Shopbutton)


#scrolling is not possible us9ing Selenium hence we use the javascript executor in that case
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

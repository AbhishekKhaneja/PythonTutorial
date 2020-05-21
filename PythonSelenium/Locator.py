#customized Xpath syntax
#//tagname[@attribute='value']---Tagname Optional
#Reg Ex : //*[contains(@attribute,'value')]

#Genarating CSS by id
# tagname#ID--tagname optional

#Generating Css From ClassName
#tagname.classname

#generating Xpath based on text
#  //tagname[text()='xxx']

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\abhkhane\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("https://login.salesforce.com")
driver.find_element_by_css_selector("#username").send_keys("Abhishek")
driver.find_element_by_css_selector(".password").send_keys("khaneja")
driver.find_element_by_link_text("Forgot Your Password?").click()

driver.find_element_by_xpath("//a[text()='Cancel']").click()

#parentchildcombination using Xpath
usernametext=driver.find_element_by_xpath("//div[@id='usernamegroup']/label").text
print(usernametext)
#parentchildcombination using Cssselector
usernametxt=driver.find_element_by_css_selector("div[id='usernamegroup'] label").text
print(usernametxt)

print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)
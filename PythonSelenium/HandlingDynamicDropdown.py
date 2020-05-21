import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\abhkhane\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.makemytrip.com/")
driver.find_element_by_id("fromCity").click()
driver.find_element_by_css_selector("div[class='hsw_autocomplePopup autoSuggestPlugin'] input").send_keys("jaip")
Cities=driver.find_elements_by_xpath("//p[@class='font14 appendBottom5 blackText']")
time.sleep(2) #same as thread.sleep in java
print(len(Cities)) # to get the length of cities retrieved use len() method which is nothing but length
for i in Cities:
    if i.text =="Jaipur, India":
        i.click()
        break #reason why we have used break here is to come out of the loop as soon as it get the desired match in the if statement otherwise it will continue to iterate till the end.

#driver.quit()
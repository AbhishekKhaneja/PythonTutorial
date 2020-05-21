from selenium import webdriver

Chromeoptions=webdriver.ChromeOptions()
Chromeoptions.add_argument("--start-maximized")
Chromeoptions.add_argument("headless") #headless means no browser is opened
Chromeoptions.add_argument("--ignore-certificate-errors") #ignore the certifiacte errors of the website if any

driver = webdriver.Chrome(executable_path="C:\\Users\\abhkhane\\Downloads\\chromedriver_win32\\chromedriver.exe",options=Chromeoptions)

driver.get("https://rahulshettyacademy.com/angularpractice/")


print(driver.title)
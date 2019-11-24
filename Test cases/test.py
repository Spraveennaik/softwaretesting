from selenium import webdriver

browser = webdriver.Edge('C:/Program Files/Webdrivers/MicrosoftWebDriver')
browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

browser.close()

from selenium import webdriver

browser = webdriver.Chrome('C:/Program Files/Webdrivers/chromedriver')
browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

browser.close()

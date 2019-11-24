from selenium import webdriver

browser = webdriver.Ie('C:/Program Files/Webdrivers/IEDriverServer')
browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

browser.close()

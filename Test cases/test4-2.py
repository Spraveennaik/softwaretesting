from selenium import webdriver

browser = webdriver.Firefox()
browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

browser.close()


from selenium import webdriver

browser = webdriver.Safari()
browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

browser.close()

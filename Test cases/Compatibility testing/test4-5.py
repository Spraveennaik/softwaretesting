from selenium import webdriver
import time
browser = webdriver.Chrome('C:/Program Files/Webdrivers/chromedriver')

browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
browser.find_element_by_xpath('//*[@id="txtUsername"]').send_keys("Admin")
browser.find_element_by_xpath('//*[@id="txtPassword"]').send_keys("admin123")
browser.find_element_by_xpath('//*[@id="btnLogin"]').click()
time.sleep(3)
browser.close()



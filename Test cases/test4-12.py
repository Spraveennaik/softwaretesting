from selenium import webdriver
import time

driver = webdriver.safari()
driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

driver.find_element_by_id("txtUsername").clear()
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").clear()
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Register OAuth Client'])[1]/following::b[1]").click()
time.sleep(3)
driver.close()
    


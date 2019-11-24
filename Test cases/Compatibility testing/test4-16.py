from selenium import webdriver

driver = webdriver.Ie('C:/Program Files/Webdrivers/IEDriverServer')

driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
driver.find_element_by_id("txtUsername").clear()
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").clear()
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Register OAuth Client'])[1]/following::b[1]").click()
driver.find_element_by_link_text("Linda").click()
driver.find_element_by_id("btnSave").click()
driver.find_element_by_id("personal_txtEmpFirstName").click()
# ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=personal_txtEmpFirstName | ]]
driver.find_element_by_id("personal_txtEmpFirstName").clear()
driver.find_element_by_id("personal_txtEmpFirstName").send_keys("manoj")
driver.find_element_by_id("btnSave").click()
driver.close()
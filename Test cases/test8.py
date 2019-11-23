
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Test8(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_8(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        driver.find_element_by_id("txtUsername").clear()
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").clear()
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Register OAuth Client'])[1]/following::b[1]").click()
        driver.find_element_by_id("menu_pim_Configuration").click()
        driver.find_element_by_id("menu_pim_listCustomFields").click()
        driver.find_element_by_id("buttonAdd").click()
        driver.find_element_by_id("customField_name").click()
        driver.find_element_by_id("customField_name").clear()
        driver.find_element_by_id("customField_name").send_keys("Phone")
        driver.find_element_by_id("customField_screen").click()
        Select(driver.find_element_by_id("customField_screen")).select_by_visible_text("Contact Details")
        driver.find_element_by_id("customField_screen").click()
        driver.find_element_by_id("customField_type").click()
        Select(driver.find_element_by_id("customField_type")).select_by_visible_text("Text or Number")
        driver.find_element_by_id("customField_type").click()
        driver.find_element_by_id("btnSave").click()
        driver.close()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

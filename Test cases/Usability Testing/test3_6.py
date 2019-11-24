from selenium import webdriver
from time import sleep
from UsabilityTest import UsabilityTest
import os


def check_file(substr):
	path = "C:\\Users\\appa_\\Downloads"

	for r, d, f in os.walk(path):
		for file in f:
			if file.find(substr):
				return True

	return False


class UsabilityCase(UsabilityTest):
	def __init__(self):
		super().__init__()
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(5)
		self.verificationErrors = []
		self.accept_next_alert = True
		self.driver.maximize_window()

	def SetUp(self):
		driver = self.driver
		driver.get("https://opensource-demo.orangehrmlive.com/")
		driver = self.driver
		driver.find_element_by_id("frmLogin").click()
		driver.find_element_by_xpath(
			"(.//*[normalize-space(text()) and normalize-space(.)='LOGIN Panel'])[1]/following::span[1]").click()
		driver.find_element_by_id("txtUsername").clear()
		driver.find_element_by_id("txtUsername").send_keys("Admin")
		driver.find_element_by_id("txtPassword").clear()
		driver.find_element_by_id("txtPassword").send_keys("admin123")
		driver.find_element_by_id("frmLogin").submit()

	def Main(self):
		driver = self.driver
		driver.get("https://opensource-demo.orangehrmlive.com/index.php/maintenance/accessEmployeeData")
		driver.find_element_by_id("confirm_password").click()
		driver.find_element_by_id("confirm_password").clear()
		driver.find_element_by_id("confirm_password").send_keys("admin123")
		driver.find_element_by_id("frmPurgeEmployeeAuthenticate").submit()
		driver.find_element_by_xpath(
			"(.//*[normalize-space(text()) and normalize-space(.)='Download Personal Data'])[1]/following::ol[1]").click()
		driver.find_element_by_id("employee_empName").click()
		driver.find_element_by_id("employee_empName").clear()
		driver.find_element_by_id("employee_empName").send_keys("jas")
		driver.find_element_by_xpath(
			"(.//*[normalize-space(text()) and normalize-space(.)='OrangeHRM, Inc'])[1]/following::li[1]").click()
		driver.find_element_by_xpath("//input[@value='Search']").click()
		driver.find_element_by_id("btnDelete").click()
		driver.find_element_by_id("modal_confirm").click()

		if not check_file("Jasmine Morgan"):
			raise Exception("File download error")

	def TearDown(self):
		sleep(2)
		self.driver.quit()


if __name__ == "__main__":
	case = UsabilityCase()
	case.execute()

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from SystemTest import SystemTest


class SystestCase(SystemTest):
	def __init__(self):
		super().__init__()
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(5)
		self.verificationErrors = []
		self.accept_next_alert = True

	def SetUp(self):
		driver = self.driver
		driver.get("https://opensource-demo.orangehrmlive.com/")
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
		driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/viewModules")
		driver.find_element_by_id("btnSave").click()
		driver.find_element_by_id("moduleConfig_time").click()
		driver.find_element_by_id("moduleConfig_performance").click()
		driver.find_element_by_id("moduleConfig_directory").click()
		driver.find_element_by_id("btnSave").click()

		e = False
		try:
			driver.find_element_by_id("menu_time_viewTimeModule")
		except:
			e = True

		if not e:
			raise Exception("System testing for disabling componenets failed")

		e = False
		try:
			driver.find_element_by_id("menu__Performance")
		except:
			e = True

		if not e:
			raise Exception("System testing for disabling componenets failed")

		e = False
		try:
			driver.find_element_by_id("menu_directory_viewDirectory")
		except:
			e = True

		if not e:
			raise Exception("System testing for disabling componenets failed")

	def TearDown(self):
		sleep(1)
		self.driver.quit()


if __name__ == "__main__":
	case = SystestCase()
	case.execute()

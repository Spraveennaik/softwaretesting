from selenium import webdriver
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

	def Main(self):
		driver = self.driver
		driver.find_element_by_id('divLogo')
		driver.find_element_by_id("frmLogin").click()
		driver.find_element_by_xpath(
			"(.//*[normalize-space(text()) and normalize-space(.)='LOGIN Panel'])[1]/following::span[1]")
		driver.find_element_by_id("txtUsername")
		driver.find_element_by_id("txtPassword")
		driver.find_element_by_id("frmLogin")

	def TearDown(self):
		sleep(1)
		self.driver.quit()


if __name__ == "__main__":
	case = SystestCase()
	case.execute()
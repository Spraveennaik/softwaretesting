from selenium import webdriver
from time import sleep
from UsabilityTest import UsabilityTest


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
		driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/viewModules")

		btns = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol').find_elements_by_tag_name('input')

		for btn in btns:
			btn.click()
			# initially they were on
			if btn.get_attribute('value') == 'off':
				raise Exception("Disabled button enabled")

	def TearDown(self):
		sleep(2)
		self.driver.quit()


if __name__ == "__main__":
	case = UsabilityCase()
	case.execute()

	# https://opensource-demo.orangehrmlive.com/index.php/admin/viewModules
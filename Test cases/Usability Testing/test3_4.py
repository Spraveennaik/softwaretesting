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
		driver.get("https://opensource-demo.orangehrmlive.com/index.php/recruitment/viewCandidates")

		driver.set_window_size(480, 320)
		c_w = driver.execute_script("return document.body.clientWidth")
		c_h = driver.execute_script("return document.body.clientHeight")
		w_w = driver.execute_script("return window.innerWidth")
		w_h = driver.execute_script("return window.innerHeight")

		if w_w >= c_w and w_h >= c_h:
			raise Exception("Scroll Bar disabled")

	def TearDown(self):
		sleep(2)
		self.driver.quit()


if __name__ == "__main__":
	case = UsabilityCase()
	case.execute()
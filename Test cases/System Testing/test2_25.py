from selenium import webdriver
from time import sleep
from SystemTest import SystemTest
import random
import string


def randomString(l = 10):
	letters = string.ascii_letters
	return ''.join(random.choice(letters) for i in range(l))


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
		username = randomString(12)
		driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/saveSystemUser")
		driver.find_element_by_id("systemUser_employeeName_empName").click()
		driver.find_element_by_id("systemUser_employeeName_empName").clear()
		driver.find_element_by_id("systemUser_employeeName_empName").send_keys("John Smith")
		driver.find_element_by_id("systemUser_userName").click()
		driver.find_element_by_id("systemUser_userName").clear()
		driver.find_element_by_id("systemUser_userName").send_keys(username)
		driver.find_element_by_id("systemUser_password").click()
		driver.find_element_by_id("systemUser_password").clear()
		driver.find_element_by_id("systemUser_password").send_keys("abcdefgh")
		driver.find_element_by_id("systemUser_confirmPassword").clear()
		driver.find_element_by_id("systemUser_confirmPassword").send_keys("abcdefgh")
		sleep(5)
		driver.find_element_by_id("btnSave").click()
		sleep(5)
		driver.find_element_by_id("MP_btn").click()
		driver.find_element_by_id("welcome").click()
		driver.find_element_by_link_text("Logout").click()

		driver.find_element_by_id("txtUsername").clear()
		driver.find_element_by_id("txtUsername").send_keys(username)
		driver.find_element_by_id("txtPassword").clear()
		driver.find_element_by_id("txtPassword").send_keys("abcdefgh")
		driver.find_element_by_id("frmLogin").submit()

		c = False

		try:
			driver.find_element_by_id("menu_dashboard_index")
		except:
			c = True

		if c:
			raise Exception("System testing Failed")

	def TearDown(self):
		sleep(1)
		self.driver.quit()


if __name__ == "__main__":
	case = SystestCase()
	case.execute()

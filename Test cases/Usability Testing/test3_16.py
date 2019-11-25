from selenium import webdriver
from UsabilityTest import UsabilityTest
import random
import string


def randomString(l = 10):
	letters = string.ascii_letters
	return ''.join(random.choice(letters) for i in range(l))


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
		driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")

		image_elements = driver.find_elements_by_tag_name("a")
		links = set()

		for img_element in image_elements:
			l = str(img_element.get_attribute('href'))
			if l != 'None' or 'orangehrm.com' not in l:
				links.add(l)

		base_url = "https://opensource-demo.orangehrmlive.com/"

		print(links)
		for link in links:
			driver.get(link)

	def TearDown(self):
		self.driver.quit()


if __name__ == "__main__":
	case = UsabilityCase()
	case.execute()

	# https://opensource-demo.orangehrmlive.com/index.php/admin/viewModules
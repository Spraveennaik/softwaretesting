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
		driver.get("https://opensource-demo.orangehrmlive.com/index.php/leave/assignLeave")

		driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[1]/input[1]').clear()
		driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[1]/input[1]').send_keys('Jasmine Morgan')
		driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/p/input').click()

		driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[2]/select').send_keys('FMLA US')
		driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/p/input').click()

		driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[4]/input').clear()
		driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[4]/input').send_keys('2019-11-15')
		driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/p/input').click()

		driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[5]/input').clear()
		driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[5]/input').send_keys('2019-11-18')

		driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/p/input').click()

	def TearDown(self):
		sleep(2)
		self.driver.quit()


if __name__ == "__main__":
	case = UsabilityCase()
	case.execute()
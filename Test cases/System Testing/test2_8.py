from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from SystemTest import SystemTest


def hover(driver, el):
	ActionChains(driver).move_to_element(el).perform()


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
		el = driver.find_element_by_id('menu_leave_viewLeaveModule')
		hover(driver, el)

		sub_els = driver.find_elements_by_xpath('/html/body/div[1]/div[2]/ul/li[3]/ul/li')
		sub_tabs_required = ['Entitlements', 'Reports', 'Configure', 'Leave List', 'Assign Leave']
		sub_tabs_present = []

		for sub_el in sub_els:
			sub_el_str = str(sub_el.text)
			sub_tabs_present = [*sub_tabs_present, *sub_el_str.split('\n')]

		for sub_tab in sub_tabs_required:
			if sub_tab not in sub_tabs_present:
				raise Exception("Sub component absent")

	def TearDown(self):
		sleep(1)
		self.driver.quit()


if __name__ == "__main__":
	case = SystestCase()
	case.execute()
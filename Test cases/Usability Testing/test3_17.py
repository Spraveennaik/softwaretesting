from selenium import webdriver
from time import sleep
from UsabilityTest import UsabilityTest
import random


def check_boundary(obj1, obj2):
	delta = 200
	if obj1['x_1'] < 0 or obj1['y_1'] < 0:
		return True
	if obj1['x_1'] - delta <= obj2['x_1'] <= obj1['x_2'] + delta and obj1['x_1'] - delta <= obj2['x_2'] <= obj1['x_2'] + \
			delta and obj1['y_1'] - delta <= obj2['y_1'] <= obj1['y_2'] + delta and obj1['y_1'] - delta <= obj2['y_2'] <= obj1['y_2'] + delta:
		return True
	if obj1['x_2'] <= obj1['x_1'] or obj1['y_2'] <= obj1['y_1']:
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
		driver.get("https://opensource-demo.orangehrmlive.com/index.php/leave/assignLeave")
		ol = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol")
		els = ol.find_elements_by_tag_name("input")
		location_array = []

		for el in els:
			d = dict()
			d['x_1'] = el.location['x']
			d['x_2'] = d['x_1'] + el.size['width']
			d['y_1'] = el.location['y']
			d['y_2'] = d['y_1'] + el.size['height']
			location_array.append(d)

		for i in range(len(location_array) - 1):
			for j in range(i+1, len(location_array)):
				if not(check_boundary(location_array[i], location_array[j]) or check_boundary(location_array[j], location_array[i])):
					raise Exception("Intersecting components")

	def TearDown(self):
		sleep(1)
		self.driver.quit()


if __name__ == "__main__":
	case = UsabilityCase()
	case.execute()
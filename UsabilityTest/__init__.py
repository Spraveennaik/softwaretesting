import time

current_milli_time = lambda: int(round(time.time() * 1000))


class UsabilityTest:
	def __init__(self, setup=None, main=None, teardown=None):
		self.setup = setup
		self.main = main
		self.teardown = teardown

	def SetUp(self):
		pass

	def Main(self):
		pass

	def TearDown(self):
		pass

	def execute(self):
		c = 0
		t1 = current_milli_time()
		try:
			if self.setup is not None:
				self.setup()
			else:
				self.SetUp()
		except BaseException as e:
			c += 1
			print("Setup Error : " + str(e))
		try:
			if self.main is not None:
				self.main()
			else:
				self.Main()
		except BaseException as e:
			c += 1
			print("Main Error : " + str(e))
		try:
			if self.teardown is not None:
				self.teardown()
			else:
				self.TearDown()
		except BaseException as e:
			c += 1
			print("TearDown Error : " + str(e))

		t1 = current_milli_time() - t1
		res = "Test Passed"
		if c > 0:
			res = "Test Failed"
		print("Execution Results:\nNumber of errors: %d\nExecution Time: %d ms\nResult: %s" % (c, t1, res))

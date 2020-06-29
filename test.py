from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Chrome(r'C:\Dpapp\Chrome\ChromePortable\chromedriver.exe')
		# self.browser = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
	#
	# def tearDown(self):
	# 	self.browser.quit()

	def test(self):
		self.browser.get('http://www.baidu.com')
		self.assertIn('百度三下', self.browser.title)
		# self.fail('Finish the test!')


if __name__ == '__main__':
	unittest.main(warnings='ignore')
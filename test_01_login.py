from selenium import webdriver
import unittest
import time

class MyTest(unittest.TestCase):

	def setUp(self):
		self.dr = webdriver.Chrome()
		self.dr.maximize_window()
		self.dr.implicitly_wait(10)
		self.base_url = 'http://111.231.120.6:8000/'

	def test_login(self):
		dr =  self.dr
		dr.get(self.base_url + '/wp-login.php')
		dr.find_element_by_id('user_login').clear()
		dr.find_element_by_id('user_login').send_keys('yesterdaysnow')
		dr.find_element_by_id('user_pass').clear()
		dr.find_element_by_id('user_pass').send_keys('042518jjw')
		dr.find_element_by_id('wp-submit').click()
		now_url = dr.current_url
		self.assertIn('wp-admin',now_url)
		current_user = dr.find_element_by_class_name('display-name').text
		self.assertEqual('yesterdaysnow',current_user)
		print('登录测试成功')

	def tearDown(self):
		self.dr.quit()

if __name__ == '__main__':
	unittest.main()

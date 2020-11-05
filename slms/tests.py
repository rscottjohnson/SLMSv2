# from django.test import client
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# import unittest

# # Organize tests into classes (which inherit from unittest.TestCase) here

# class NewVisitorTest(unittest.TestCase):

#   def setUp(self):
#     self.browser = webdriver.Firefox()

#   # def tearDown(self):
#   #   self.browser.quit()

#   def test_can_view_the_log_in_page(self):
#     # User visits SLMS homepage
#     self.browser.get('http://localhost:8000')
    
#     # The Log-in page title is 'Log-in'
#     self.assertIn('Log-in', self.browser.title)

#   def test_can_log_in(self):
#     TEST_USERNAME = 'safariuser'
#     TEST_PASSWORD = 'safaripassword'
    
#     # User visits SLMS homepage
#     self.browser.get('http://localhost:8000')
    
#     # The Log-in page title is 'Log-in'
#     self.assertIn('Log-in', self.browser.title)

#     self.browser.find_element_by_name('username').send_keys(TEST_USERNAME)
#     self.browser.find_element_by_name('password').send_keys(TEST_PASSWORD)
#     self.browser.find_element_by_name('log-in-button').send_keys(Keys.ENTER)
    
#     # Fails regardless
#     # self.fail('Finish the test!')
        
# if __name__ == '__main__':
#   unittest.main(warnings='ignore')
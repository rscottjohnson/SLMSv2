from django.test import client
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User

import unittest

# Organize tests into classes (which inherit from unittest.TestCase) here

class AccountTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def test_register_new_user_log_in_log_out(self):
    # Test user credentials
    TEST_USERNAME = 'testuser2'
    TEST_FIRST_NAME = 'Test'
    TEST_EMAIL = 'testuser2@example.com'
    TEST_PASSWORD = 'testuser2password'
    # User visits SLMS register page
    self.browser.get('http://127.0.0.1:8000/account/register/')
    # The page title is 'Create account'
    self.assertIn('Create account', self.browser.title)
    # Pass in the user credentials
    self.browser.find_element_by_name('username').send_keys(TEST_USERNAME)
    self.browser.find_element_by_name('first_name').send_keys(TEST_FIRST_NAME)
    self.browser.find_element_by_name('email').send_keys(TEST_EMAIL)
    self.browser.find_element_by_name('password').send_keys(TEST_PASSWORD)
    self.browser.find_element_by_name('password2').send_keys(TEST_PASSWORD)
    self.browser.find_element_by_name('create-account-button').send_keys(Keys.ENTER)  
    # User visits SLMS homepage
    self.browser.get('http://127.0.0.1:8000')
    # The page title is now 'Log-in'
    self.assertIn('Log-in', self.browser.title)
    # Pass in the user credentials
    self.browser.find_element_by_name('username').send_keys(TEST_USERNAME)
    self.browser.find_element_by_name('password').send_keys(TEST_PASSWORD)
    self.browser.find_element_by_name('log-in-button').send_keys(Keys.ENTER)
    # User logs out
    self.browser.find_element_by_name('log-out-link').send_keys(Keys.ENTER)
    # User is taken to the Logged Out page
    self.browser.get('http://127.0.0.1:8000/account/logout/')
    # The page title is now 'Logged Out'
    self.assertIn('Logged Out', self.browser.title)
    # Delete the test user that was created
    test_user = User.objects.filter(username='testuser2')
    test_user.delete()
    # Test user should no longer be in the data set
    self.assertFalse(User.objects.filter(username='testuser2').exists())
          
if __name__ == '__main__':
  unittest.main(warnings='ignore')
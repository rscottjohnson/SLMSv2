from django.test import client
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User

import unittest

# Organize tests into classes (which inherit from unittest.TestCase) here

# OVERVIEW: AccountTest is an object for testing the account app of slms.
# The AccountTest test test cases align with Test Scenario 1.
class AccountTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()
    # Delete TC_1 user
    tc1_user = User.objects.filter(email='chromeuser@example.com')
    tc1_user.delete()

  # TC_1
  def test_register_new_user_with_valid_inputs(self):
    # MODIFIES: User model
    # EFFECTS: Adds a new user to the User table when given valid inputs

    # Test data
    TEST_USERNAME = 'chromeuser'
    TEST_FIRST_NAME = 'Chrome'
    TEST_EMAIL = 'chromeuser@example.com'
    TEST_PASSWORD = 'chromeuserpassword'
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

    WebDriverWait(self.browser, 10).until(EC.url_matches('http://127.0.0.1:8000/account/register/'))
    # Account now exists
    self.assertTrue(User(username=TEST_USERNAME))

  # TC_2
  def test_register_new_user_with_invalid_inputs(self):
    # EFFECTS: Messages to the user pointing out invalid inputs

    # Test data
    TEST_USERNAME = 'firefoxuser'
    TEST_FIRST_NAME = ''
    TEST_EMAIL = 'firefoxuser@example.com'
    TEST_PASSWORD = ''
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
    # Remain on 'Create account' page
    self.assertIn('Create account', self.browser.title)
    # Account not created
    self.assertFalse(User.objects.filter(username=TEST_USERNAME))

  # TC_3
  def test_login_user_with_valid_inputs(self):
    # EFFECTS: Redirects logged in user to the User Dashboard

    # Test data
    TEST_USERNAME = 'safariuser'
    TEST_PASSWORD = 'safaripassword'
    # User visits SLMS register page
    self.browser.get('http://127.0.0.1:8000/')
    # The page title is 'Log-in'
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

  # TC_4
  def test_login_user_with_invalid_inputs(self):
    # EFFECTS: Redirects logged in user to the User Dashboard

    # Test data
    TEST_USERNAME = 'safariuser'
    TEST_PASSWORD = ''
    # User visits SLMS register page
    self.browser.get('http://127.0.0.1:8000/')
    # The page title is 'Log-in'
    self.assertIn('Log-in', self.browser.title)
    # Pass in the user credentials
    self.browser.find_element_by_name('username').send_keys(TEST_USERNAME)
    self.browser.find_element_by_name('password').send_keys(TEST_PASSWORD)
    self.browser.find_element_by_name('log-in-button').send_keys(Keys.ENTER)
    # The page title is still 'Log-in'
    self.assertIn('Log-in', self.browser.title)
          
if __name__ == '__main__':
  unittest.main(warnings='ignore')
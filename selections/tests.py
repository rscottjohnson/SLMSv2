from django.contrib.auth import BACKEND_SESSION_KEY, SESSION_KEY, authenticate
from django.test import client
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User
from .models import Selection
from django.urls import reverse
from django.conf import settings
from django.test.client import Client

import unittest

# Organize tests into classes (which inherit from unittest.TestCase) here

class SelectionTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()
    # Create the test user
    user = User.objects.create_user('ts2user', 'ts2user@example.com', 'ts2userpassword')

  def tearDown(self):
    self.browser.quit()
    # Delete the test user
    ts2user = User.objects.filter(username='ts2user')
    ts2user.delete()

  def test_create_selection_as_logged_in_user_with_valid_inputs(self):
    # Test user credentials
    TEST_USERNAME = 'ts2user'
    TEST_PASSWORD = 'ts2userpassword'
    # Test lunch selection attributes
    TEST_LUNCH_TYPE = 'Cold Lunch'
    TEST_PARENT_ATTENDANCE = 'No'
    TEST_CONTENT = 'a' * 300
    # Get the view
    self.browser.get('http://127.0.0.1:8000/selections/create/')
    # Pass in the credentials
    self.browser.find_element_by_name('username').send_keys(TEST_USERNAME)
    self.browser.find_element_by_name('password').send_keys(TEST_PASSWORD)
    self.browser.find_element_by_name('password').send_keys(Keys.ENTER)
    # Wait for the url to change
    WebDriverWait(self.browser, 10).until(EC.url_matches('http://127.0.0.1:8000/selections/create/'))
    # The page title has changed
    self.assertIn('Make a selection', self.browser.title)
    # Pass in the new selection attributes
    self.browser.find_element_by_name('lunch_type').send_keys(TEST_LUNCH_TYPE)
    self.browser.find_element_by_name('parent_attendance').send_keys(TEST_PARENT_ATTENDANCE)
    self.browser.find_element_by_name('content').send_keys(TEST_CONTENT)
    self.browser.find_element_by_name('make-selection-button').send_keys(Keys.ENTER)
    # Selection now exists
    self.assertTrue(Selection(content=TEST_CONTENT))

  def test_create_selection_as_non_logged_in_user_with_valid_inputs(self):
    # Get the view
    self.browser.get('http://127.0.0.1:8000/selections/create/')
    # The page title remains at the log-in page
    self.assertIn('Log-in', self.browser.title)
   
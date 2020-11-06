from django.contrib.auth import BACKEND_SESSION_KEY, SESSION_KEY
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

  def tearDown(self):
    self.browser.quit()

  def test_selection_create(self):
    # Test user credentials
    TEST_USERNAME = 'safariuser'
    TEST_PASSWORD = 'safaripassword'
    # Test lunch selection attributes
    TEST_LUNCH_TYPE = 'Cold Lunch'
    TEST_PARENT_ATTENDANCE = 'No'
    TEST_CONTENT = 'test_selection_create content'
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
    # The content of the new selection is now included
    self.assertTrue(Selection.objects.all().filter(content='test_selection_create content').exists())
        
  def test_selection_list(self):
    # Test user credentials
    TEST_USERNAME = 'safariuser'
    TEST_PASSWORD = 'safaripassword'
    # Get the view
    self.browser.get('http://127.0.0.1:8000/selections/')
    # Pass in the credentials
    self.browser.find_element_by_name('username').send_keys(TEST_USERNAME)
    self.browser.find_element_by_name('password').send_keys(TEST_PASSWORD)
    self.browser.find_element_by_name('password').send_keys(Keys.ENTER)
    # Wait for the url to change
    WebDriverWait(self.browser, 10).until(EC.url_matches('http://127.0.0.1:8000/selections/'))
    # The page title has changed
    self.assertIn('Selections made', self.browser.title)
    
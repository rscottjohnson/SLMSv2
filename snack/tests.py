from django.test import TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from .models import Count

# Create your tests here.

class SnackTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def test_count_list(self):
    # Get the view
    self.browser.get('http://127.0.0.1:8000/snack/')
    # The page title has changed
    self.assertIn('Snack Counts', self.browser.title)

  def test_count_create(self):
    # Test user credentials
    TEST_USERNAME = 'safariuser'
    TEST_PASSWORD = 'safaripassword'
    # Test lunch selection attributes
    TEST_COUNT_TITLE = 'TEST COUNT'
    TEST_COUNT_FOOD = "Welch's Fruit Snacks - Mixed Fruit"
    TEST_COUNT_QUANTITY = 50
    TEST_COUNT_BODY = 'test_count_create content'
    TEST_COUNT_STATUS = 'Published'
    # Get the view
    self.browser.get('http://127.0.0.1:8000/snack/create/')
    # Pass in the credentials
    self.browser.find_element_by_name('username').send_keys(TEST_USERNAME)
    self.browser.find_element_by_name('password').send_keys(TEST_PASSWORD)
    self.browser.find_element_by_name('password').send_keys(Keys.ENTER)
    # Wait for the url to change
    WebDriverWait(self.browser, 10).until(EC.url_matches('http://127.0.0.1:8000/snack/create/'))
    # The page title has changed
    self.assertIn('Create Snack Count', self.browser.title)
    # Pass in the new count attributes
    self.browser.find_element_by_name('title').send_keys(TEST_COUNT_TITLE)
    self.browser.find_element_by_name('food').send_keys(TEST_COUNT_FOOD)
    self.browser.find_element_by_name('quantity').send_keys(TEST_COUNT_QUANTITY)
    self.browser.find_element_by_name('body').send_keys(TEST_COUNT_BODY)
    self.browser.find_element_by_name('status').send_keys(TEST_COUNT_STATUS)
    self.browser.find_element_by_name('create-count-button').send_keys(Keys.ENTER)
    # The content of the new count is now included
    self.assertTrue(Count.objects.filter(title='TEST COUNT').exists())
  
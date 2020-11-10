from django.test import TestCase, RequestFactory
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from .models import Count, Food
from .views import count_list, count_create, count_edit
from django.contrib.auth.models import User
import random
from random import randrange
import string

# Create your tests here.

# OVERVIEW: SnackTest is an object for testing the snack app of slms.
# The SnackTest test cases align with Test Scenario 3.
class SnackTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()
    # Create the test user
    user = User.objects.create_user('ts3user', 'ts3user@example.com', 'ts3userpassword')

  def tearDown(self):
    self.browser.quit()
    # Delete the test user
    ts3user = User.objects.filter(username='ts3user')
    ts3user.delete()

  # TC_1
  def test_count_list(self):
    # EFFECTS: Lists the current view of snack counts

    # Get the view
    self.browser.get('http://127.0.0.1:8000/snack/')
    # The page title has changed
    self.assertIn('Snack Counts', self.browser.title)

  # TC_2
  def test_create_count_as_logged_in_user_with_valid_inputs(self):
    # MODIFIES: Count model
    # EFFECTS: Adds a new snack count to the Count table when given valid inputs

    # Test user credentials
    TEST_USERNAME = 'ts3user'
    TEST_PASSWORD = 'ts3userpassword'
    # Test lunch selection attributes
    TEST_COUNT_TITLE = 'TEST COUNT VALID'
    letters = string.ascii_lowercase
    TEST_COUNT_FOOD = Food.objects.get(pk=1).description
    TEST_COUNT_QUANTITY = random.randint(1, 100)
    TEST_COUNT_BODY = ''.join(random.choice(letters) for i in range(50))
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
    self.assertTrue(Count(title=TEST_COUNT_TITLE))

  # TC_3
  def test_create_count_as_logged_in_user_with_invalid_title(self):
    # EFFECTS:  Messages to the user pointing out invalid inputs

    # Test user credentials
    TEST_USERNAME = 'ts3user'
    TEST_PASSWORD = 'ts3userpassword'
    # Test lunch selection attributes
    TEST_COUNT_TITLE = 'a' * 251
    letters = string.ascii_lowercase
    TEST_COUNT_FOOD = Food.objects.get(pk=1).description
    TEST_COUNT_QUANTITY = random.randint(1, 100)
    TEST_COUNT_BODY = ''.join(random.choice(letters) for i in range(50))
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
    self.assertTrue(Count(title=TEST_COUNT_TITLE))

  # TC_4
  def test_create_count_as_logged_in_user_with_invalid_quantity(self):
    # EFFECTS:  Messages to the user pointing out invalid inputs

    # Test user credentials
    TEST_USERNAME = 'ts3user'
    TEST_PASSWORD = 'ts3userpassword'
    # Test lunch selection attributes
    TEST_COUNT_TITLE = 'TEST COUNT QTY'
    letters = string.ascii_lowercase
    TEST_COUNT_FOOD = Food.objects.get(pk=1).description
    TEST_COUNT_QUANTITY = random.randint(-100, -1)
    TEST_COUNT_BODY = ''.join(random.choice(letters) for i in range(50))
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
    self.assertTrue(Count(title=TEST_COUNT_TITLE))

  # TC_5
  def test_edit_count_as_logged_in_user_with_valid_inputs(self):
    # MODIFIES: Count model
    # EFFECTS:  Edits a new snack count in the Count table when given valid inputs
    
    # Test user credentials
    TEST_USERNAME = 'ts3user'
    TEST_PASSWORD = 'ts3userpassword'
    TEST_COUNT_SLUG = str(Count.objects.last().slug)
    TEST_COUNT_ID = str(Count.objects.last().id)
    TEST_COUNT_TITLE = str(Count.objects.last().title)
    TEST_COUNT_YEAR = str(Count.objects.last().publish.year)
    TEST_COUNT_MONTH = str(Count.objects.last().publish.month)
    TEST_COUNT_DAY = str(Count.objects.last().publish.day)
    # TEST_COUNT = str(TEST_COUNT)
    letters = string.ascii_lowercase
    TEST_COUNT_BODY = ''.join(random.choice(letters) for i in range(50))
    # TEST_COUNT_STATUS = 'Draft'
    # Get the view
    self.browser.get('http://127.0.0.1:8000/snack/' + TEST_COUNT_ID + '/edit/')
    # Pass in the credentials
    self.browser.find_element_by_name('username').send_keys(TEST_USERNAME)
    self.browser.find_element_by_name('password').send_keys(TEST_PASSWORD)
    self.browser.find_element_by_name('password').send_keys(Keys.ENTER)
    # Wait for the url to change
    WebDriverWait(self.browser, 10).until(EC.url_matches('http://127.0.0.1:8000/snack/' + TEST_COUNT_ID + '/edit/'))
    # The page title has changed
    self.assertIn('Edit Snack Count', self.browser.title)
    # Pass in the new count attributes
    self.browser.find_element_by_name('body').send_keys(TEST_COUNT_BODY)
    # self.browser.find_element_by_name('status').send_keys(TEST_COUNT_STATUS)
    self.browser.find_element_by_name('edit-count-button').send_keys(Keys.ENTER)
    # Wait for the url to change
    WebDriverWait(self.browser, 10).until(EC.url_matches('http://127.0.0.1:8000/snack/' + TEST_COUNT_YEAR + '/' + TEST_COUNT_MONTH + '/' + TEST_COUNT_DAY + '/' + TEST_COUNT_SLUG + '/'))
    # The page title has changed
    self.assertIn(TEST_COUNT_TITLE, self.browser.title)
  
  # TC_6
  def test_edit_count_as_logged_in_user_with_invalid_quantity(self):
    # EFFECTS:  Messages to the user pointing out invalid inputs

    # Test user credentials
    TEST_USERNAME = 'ts3user'
    TEST_PASSWORD = 'ts3userpassword'
    TEST_COUNT = str(Count.objects.last().id)
    # TEST_COUNT = str(TEST_COUNT)
    letters = string.ascii_lowercase
    TEST_COUNT_QUANTITY = random.randint(-100, -1)
    # TEST_COUNT_STATUS = 'Draft'
    # Get the view
    self.browser.get('http://127.0.0.1:8000/snack/' + TEST_COUNT + '/edit/')
    # Pass in the credentials
    self.browser.find_element_by_name('username').send_keys(TEST_USERNAME)
    self.browser.find_element_by_name('password').send_keys(TEST_PASSWORD)
    self.browser.find_element_by_name('password').send_keys(Keys.ENTER)
    # Wait for the url to change
    WebDriverWait(self.browser, 10).until(EC.url_matches('http://127.0.0.1:8000/snack/' + TEST_COUNT + '/edit/'))
    # The page title has changed
    self.assertIn('Edit Snack Count', self.browser.title)
    # Pass in the new count attributes
    self.browser.find_element_by_name('quantity').send_keys(TEST_COUNT_QUANTITY)
    # self.browser.find_element_by_name('status').send_keys(TEST_COUNT_STATUS)
    self.browser.find_element_by_name('edit-count-button').send_keys(Keys.ENTER)
    # The page title has not changed
    self.assertIn('Edit Snack Count', self.browser.title)
  
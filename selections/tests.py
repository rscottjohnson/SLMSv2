from django.test import client
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User

import unittest

# Organize tests into classes (which inherit from unittest.TestCase) here

class SelectionTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def test_selection_create(self):
  
  def test_selection_detail(self):
  
  def test_selection_like(self):
  
  def test_selection_list(self):

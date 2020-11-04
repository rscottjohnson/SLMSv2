from selenium import webdriver
import unittest

# Organize tests into classes (which inherit from unittest.TestCase) here

class NewVisitorTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def test_can_start_a_list_and_retrieve_it_later(self):
    # User visits SLMS homepage
    self.browser.get('http://localhost:8000')
    
    # The Log-in page title is 'Log-in'
    self.assertIn('Log-in', self.browser.title)
    
    # Fails regardless
    self.fail('Finish the test!')
    
if __name__ == '__main__':
  unittest.main(warnings='ignore')
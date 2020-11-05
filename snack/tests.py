from django.test import TestCase

# Create your tests here.

def test_staff_can_add_food(self):
  """
  Tests that a staff user can access the Snack Food Dashboard and add a new Food
  """
  # Staff user would like to access the Snack Dashboard and add a new Food.
  # She visits the log-in page
  root = self.browser.get(self.live_server_url + '/')

  # She verifies the page title
  self.assertEqual(self.browser.title, 'Log-in')

  # She enters her username and password and submits the form to log-in

  # She clicks on the Snack Dashboard link to visit the Snack Dashboard page to see
  # all of the snack foods that have been added so far

  # She verifies the page title

  # She adds a snack food

  self.fail('Incomplete Test')

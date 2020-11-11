from django.contrib.auth.models import User
from .models import Selection
from django.urls import reverse
from django.test import TestCase
import random
import string

# Organize tests here

# OVERVIEW: SnackFoodTest is an object for testing the snack app of slms.
# The SnackFoodTest test cases align with Test Scenario 2.
class TestLunchSelection(TestCase):

  def setUp(self):
    self.staff_user = User.objects.create_superuser('staff_user', 'staffuser@example.com', 'staffuserpassword')
    self.non_staff_user = User.objects.create_user('non_staff_user', 'nonstaffuser@example.com', 'nonstaffuserpassword')

  def tearDown(self):
    self.staff_user.delete()

  def test_anonymous_user_cannot_access_create_selection(self):
    response = self.client.get(reverse("selections:create"))
    self.assertRedirects(response, "/account/login/?next=/selections/create/")

  def test_authenticated_non_staff_user_cannot_access_create_selection(self):
    self.client.force_login(user=self.non_staff_user)
    response = self.client.get(reverse("selections:create"))
    self.assertNotEqual(response.status_code, 200)

  def test_authenticated_staff_user_can_access_create_selection(self):
    self.client.force_login(user=self.staff_user)
    response = self.client.get(reverse("selections:create"))
    self.assertEqual(response.status_code, 200)

  def test_authenticated_staff_user_can_create_selection_with_valid_inputs(self):
    self.client.force_login(user=self.staff_user)
    selection_count = Selection.objects.all().count()
    lt_choice_list = ['HOT LUNCH', 'COLD LUNCH', 'FIELD TRIP LUNCH']
    pa_choice_list = ['YES', 'NO']
    letters = string.ascii_lowercase
    response = self.client.post('/selections/create/', {'lunch_type': random.choice(lt_choice_list), 'parent_attendance': random.choice(pa_choice_list), 'content': ''.join(random.choice(letters) for i in range(20))})
    self.assertEqual(Selection.objects.all().count(), selection_count + 1)

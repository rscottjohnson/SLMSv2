from django.test import TestCase
from django.urls import reverse
from .models import Food
from django.contrib.auth.models import User
import random
import string

# Create your tests here.

# OVERVIEW: TestSnackFood is an object for testing the snack app of slms.
# The TestSnackFood test cases align with Test Scenario 3.
class TestSnackFood(TestCase):

  def setUp(self):
    self.staff_user = User.objects.create_superuser('staff_user', 'staffuser@example.com', 'staffuserpassword')
    self.non_staff_user = User.objects.create_user('non_staff_user', 'nonstaffuser@example.com', 'nonstaffuserpassword')

  def tearDown(self):
    self.staff_user.delete()

  # TC_1
  def test_anonymous_user_cannot_access_create_food(self):
    response = self.client.get(reverse("snack:food_create"))
    self.assertRedirects(response, "/account/login/?next=/snack/list/create/")

  # TC_2
  def test_authenticated_non_staff_user_cannot_access_create_food(self):
    self.client.force_login(user=self.non_staff_user)
    response = self.client.get(reverse("snack:food_create"))
    self.assertNotEqual(response.status_code, 200)

  # TC_3
  def test_authenticated_staff_user_can_access_create_food(self):
    self.client.force_login(user=self.staff_user)
    response = self.client.get(reverse("snack:food_create"))
    self.assertEqual(response.status_code, 200)

  # TC_4
  def test_authenticated_staff_user_can_create_food_with_valid_inputs(self):
    self.client.force_login(user=self.staff_user)
    food_count = Food.objects.all().count()
    letters = string.ascii_lowercase
    response = self.client.post('/snack/list/create/', {'description': ''.join(random.choice(letters) for i in range(20)), 'category': 'bars', 'inventory': random.randint(1, 99)})
    self.assertEqual(Food.objects.all().count(), food_count + 1)

# OVERVIEW: TestSnackCount is an object for testing the snack app of slms.
# The TestSnackCount test cases align with Test Scenario 4.
class TestSnackCount(TestCase):

  def setUp(self):
    self.staff_user = User.objects.create_superuser('staff_user', 'staffuser@example.com', 'staffuserpassword')
    self.non_staff_user = User.objects.create_user('non_staff_user', 'nonstaffuser@example.com', 'nonstaffuserpassword')

  def tearDown(self):
    self.staff_user.delete()

  # TC_1
  def test_anonymous_user_cannot_access_create_count(self):
    response = self.client.get(reverse("snack:count_create"))
    self.assertRedirects(response, "/account/login/?next=/snack/create/")

  # TC_2
  def test_authenticated_non_staff_user_cannot_access_create_count(self):
    self.client.force_login(user=self.non_staff_user)
    response = self.client.get(reverse("snack:count_create"))
    self.assertNotEqual(response.status_code, 200)

  # TC_3
  def test_authenticated_staff_user_can_access_create_count(self):
    self.client.force_login(user=self.staff_user)
    response = self.client.get(reverse("snack:count_create"))
    self.assertEqual(response.status_code, 200)

  # TC_4
  # def test_authenticated_staff_user_can_create_count_with_valid_inputs(self):
  #   self.client.force_login(user=self.staff_user)
  #   # count_count_before = Count.objects.all().count()
  #   snack_count = Count.objects.count()
  #   letters = string.ascii_lowercase
  #   response = self.client.post('/snack/create/', {'title': 'test-title', 'food': 'Banana', 'quantity': random.randint(1, 20), 'body': ''.join(random.choice(letters) for i in range(20)), 'status': 'Published'})
  #   self.assertEqual(Count.objects.count(), snack_count + 1)

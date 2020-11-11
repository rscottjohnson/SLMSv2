from django.contrib.auth.models import User
from .models import Profile
from django.test import TestCase
from django.urls import reverse
import random
import string

# Organize tests here

# OVERVIEW: TestAccount is an object for testing the snack app of slms.
# The TestAccount test cases align with Test Scenario 1.
class TestAccount(TestCase):

  def setUp(self):
    st_user = User.objects.create_superuser('staff_user', 'staffuser@example.com', 'staffuserpassword')
    st_user_with_profile = Profile.objects.create(user=st_user)
    nost_user = User.objects.create_user('non_staff_user', 'nonstaffuser@example.com', 'nonstaffuserpassword')
    nost_user_with_profile = Profile.objects.create(user=nost_user)
    self.staff_user = User.objects.all().filter(is_staff=1).last()
    self.non_staff_user = User.objects.all().filter(is_staff=0).last()

  def tearDown(self):
    self.staff_user.delete()

  # User Dashboard access

  # TC_1
  def test_anonymous_user_cannot_access_user_dashboard(self):
    response = self.client.get(reverse("dashboard"))
    self.assertRedirects(response, "/account/login/?next=/account/")

  # TC_2
  def test_authenticated_non_staff_user_can_access_user_dashboard(self):
    self.client.force_login(user=self.non_staff_user)
    response = self.client.get(reverse("dashboard"))
    self.assertEqual(response.status_code, 200)

  # TC_3
  def test_authenticated_staff_user_can_access_user_dashboard(self):
    self.client.force_login(user=self.staff_user)
    response = self.client.get(reverse("dashboard"))
    self.assertEqual(response.status_code, 200)

  # User Profile access

  # TC_4
  def test_anonymous_user_cannot_access_user_profile(self):
    response = self.client.get(reverse("edit"))
    self.assertRedirects(response, "/account/login/?next=/account/edit/")

  # TC_5
  def test_authenticated_non_staff_user_can_access_user_profile(self):
    self.client.force_login(user=self.non_staff_user)
    response = self.client.get(reverse("edit"))
    self.assertEqual(response.status_code, 200)

  # TC_6
  def test_authenticated_staff_user_can_access_user_profile(self):
    self.client.force_login(user=self.staff_user)
    response = self.client.get(reverse("edit"))
    self.assertEqual(response.status_code, 200)

  # Edit user profile
  
  # TC_7  
  def test_authenticated_non_staff_user_can_edit_user_profile_with_valid_inputs(self):
    self.client.force_login(user=self.non_staff_user)
    letters = string.ascii_lowercase
    response = self.client.post('/account/edit/', {'guardian_name': ''.join(random.choice(letters) for i in range(15)), 'guardian_email': ''.join(random.choice(letters) for i in range(5)) + '@example.com'})
    self.assertContains(response, '<li class="success">')
  
  # TC_8
  def test_authenticated_non_staff_user_cannot_edit_user_profile_with_invalid_inputs(self):
    self.client.force_login(user=self.non_staff_user)
    response = self.client.post('/account/edit/', {'guardian_name': 'a' * 181})
    self.assertContains(response, '<li class="error">')

  # User password access

  # TC_9 
  def test_anonymous_user_cannot_access_change_password(self):
    response = self.client.get(reverse("password_change"))
    self.assertRedirects(response, "/account/login/?next=/account/password_change/")

  # TC_10
  def test_authenticated_non_staff_user_can_access_change_password(self):
    self.client.force_login(user=self.non_staff_user)
    response = self.client.get(reverse("password_change"))
    self.assertEqual(response.status_code, 200)

  # TC_11
  def test_authenticated_staff_user_can_access_change_password(self):
    self.client.force_login(user=self.staff_user)
    response = self.client.get(reverse("password_change"))
    self.assertEqual(response.status_code, 200)

  # User list access

  # TC_12 
  def test_anonymous_user_cannot_access_user_list(self):
    response = self.client.get(reverse("user_list"))
    self.assertRedirects(response, "/account/login/?next=/account/users/")

  # TC_13
  def test_authenticated_non_staff_user_can_access_access_user_list(self):
    self.client.force_login(user=self.non_staff_user)
    response = self.client.get(reverse("user_list"))
    self.assertEqual(response.status_code, 200)

  # TC_14
  def test_authenticated_staff_user_can_access_access_user_list(self):
    self.client.force_login(user=self.staff_user)
    response = self.client.get(reverse("user_list"))
    self.assertEqual(response.status_code, 200)
  
  # User detail access

  # TC_15
  def test_authenticated_non_staff_user_can_access_access_user_detail(self):
    self.client.force_login(user=self.non_staff_user)
    response = self.client.get(reverse("user_detail", args=[self.non_staff_user]))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, '<div class="profile-info">')

  # Register account

  # TC_16
  def test_new_user_registration_with_valid_inputs(self):
    response = self.client.get(reverse("register"))
    self.assertEqual(response.status_code, 200)
    letters = string.ascii_lowercase
    response = self.client.post('/account/register/', {'username': ''.join(random.choice(letters) for i in range(6)), 'first_name': ''.join(random.choice(letters) for i in range(6)), 'email': ''.join(random.choice(letters) for i in range(6)) + '@example.com', 'password': 'password', 'password2': 'password'})
    self.assertContains(response, '<h1>Welcome')

  # TC_17
  def test_new_user_registration_with_invalid_inputs(self):
    response = self.client.get(reverse("register"))
    self.assertEqual(response.status_code, 200)
    response = self.client.post('/account/register/', {'username': '', 'first_name': '', 'email': '', 'password': '', 'password2': ''})
    self.assertContains(response, '<h1>Create an account</h1>')

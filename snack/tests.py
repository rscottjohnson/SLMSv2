from django.test import TestCase
from django.urls import reverse
from .models import Count, Food
from django.contrib.auth.models import User
import random
import string

# Create your tests here.

# OVERVIEW: TestSnackDashboard is an object for testing the snack app of slms.
# The TestSnackFood test cases align with Test Scenario 5.
class TestSnackDashboard(TestCase):

  def setUp(self):
    self.staff_user = User.objects.create_superuser('staff_user', 'staffuser@example.com', 'staffuserpassword')
    self.non_staff_user = User.objects.create_user('non_staff_user', 'nonstaffuser@example.com', 'nonstaffuserpassword')
    self.food = Food.objects.create(description='test food', category='fruit', inventory=10)
    self.count = Count.objects.create(title='test count', food=Food.objects.get(id=1), quantity=2, body='test body', status='Published', author_id=self.staff_user.id)
    self.valid_count_inputs = {'title': 'test title', 'food': Food.objects.get(id=1), 'quantity': random.randint(1, 20), 'body': 'Test body', 'status': 'Published'}

  def tearDown(self):
    self.staff_user.delete()

  # Create snack food access

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
  
  # Create snack count access

  # TC_5
  def test_anonymous_user_cannot_access_create_count(self):
    response = self.client.get(reverse("snack:count_create"))
    self.assertRedirects(response, "/account/login/?next=/snack/create/")

  # TC_6
  def test_authenticated_non_staff_user_cannot_access_create_count(self):
    self.client.force_login(user=self.non_staff_user)
    response = self.client.get(reverse("snack:count_create"))
    self.assertNotEqual(response.status_code, 200)

  # TC_7
  def test_authenticated_staff_user_can_access_create_count(self):
    self.client.force_login(user=self.staff_user)
    response = self.client.get(reverse("snack:count_create"))
    self.assertEqual(response.status_code, 200)

  # def test_authenticated_staff_user_can_create_count_with_valid_inputs(self):
  #   self.client.force_login(user=self.staff_user)
  #   snack_count = Count.objects.count()
  #   response = self.client.post(reverse('snack:count_create'), data={'form':{'title': 'test title', 'food': 'Banana', 'quantity': 15, 'body': 'Test body', 'status': 'Published'}}, format='json', follow=True)
  #   self.assertEqual(Count.objects.count(), snack_count + 1)

  # Edit snack count access

  # TC_7
  def test_anonymous_user_cannot_access_edit_count(self):
    response = self.client.get(reverse("snack:count_edit", args=[self.count.id]))
    self.assertRedirects(response, "/account/login/?next=/snack/" + str(self.count.id) + "/edit/")
  
  def test_authenticated_non_staff_user_cannot_access_edit_count(self):
    self.client.force_login(user=self.non_staff_user)
    response = self.client.get(reverse("snack:count_edit", args=[self.count.id]))
    self.assertNotEqual(response.status_code, 200)
  
  def test_authenticated_staff_user_can_access_edit_count(self):
    self.client.force_login(user=self.staff_user)
    response = self.client.get(reverse("snack:count_edit", args=[self.count.id]))
    self.assertEqual(response.status_code, 200)

  # def test_authenticated_staff_user_can_edit_count_with_valid_inputs(self):
  #   self.client.force_login(user=self.staff_user)
  #   letters = string.ascii_lowercase
  #   response = self.client.post("/snack/" + str(self.count.id) + "/edit/", {'food': Food.objects.get(id=1), 'quantity': 10, 'body': 'test body'})
  #   self.assertContains(response, '<li class="success">')

  # Count list access

  # TC_8
  def test_anonymous_user_cannot_access_count_list(self):
    response = self.client.get(reverse("snack:count_list"))
    self.assertRedirects(response, "/account/login/?next=/snack/")

  # TC_9
  def test_authenticated_non_staff_user_cannot_access_count_list(self):
    self.client.force_login(user=self.non_staff_user)
    response = self.client.get(reverse("snack:count_list"))
    self.assertNotEqual(response.status_code, 200)

  # TC_10
  def test_authenticated_staff_user_can_access_count_list(self):
    self.client.force_login(user=self.staff_user)
    response = self.client.get(reverse("snack:count_list"))
    self.assertEqual(response.status_code, 200)

  # Food list access

  # TC_11
  def test_anonymous_user_cannot_access_food_list(self):
    response = self.client.get(reverse("snack:food_list"))
    self.assertRedirects(response, "/account/login/?next=/snack/list/")

  # TC_12
  def test_authenticated_non_staff_user_cannot_access_food_list(self):
    self.client.force_login(user=self.non_staff_user)
    response = self.client.get(reverse("snack:food_list"))
    self.assertNotEqual(response.status_code, 200)

  # TC_13
  def test_authenticated_staff_user_can_access_food_list(self):
    self.client.force_login(user=self.staff_user)
    response = self.client.get(reverse("snack:food_list"))
    self.assertEqual(response.status_code, 200)
  
  # Food detail access

  # TC_4
  def test_anonymous_user_cannot_access_food_detail(self):
    response = self.client.get(reverse("snack:food_detail", args=[self.food.id]))
    self.assertRedirects(response, "/account/login/?next=/snack/list/" + str(self.food.id) + "/")

  def test_authenticated_non_staff_user_cannot_access_food_detail(self):
    self.client.force_login(user=self.non_staff_user)
    response = self.client.get(reverse("snack:food_detail", args=[self.food.id]))
    self.assertNotEqual(response.status_code, 200)

  def test_authenticated_staff_user_can_access_food_detail(self):
    self.client.force_login(user=self.staff_user)
    response = self.client.get(reverse("snack:food_detail", args=[self.food.id]))
    self.assertEqual(response.status_code, 200)
  
  # Food edit access

  def test_anonymous_user_cannot_edit_food(self):
    response = self.client.get(reverse("snack:food_edit", args=[self.food.id]))
    self.assertRedirects(response, "/account/login/?next=/snack/list/" + str(self.food.id) + "/edit/")

  def test_authenticated_non_staff_user_cannot_edit_food(self):
    self.client.force_login(user=self.non_staff_user)
    response = self.client.get(reverse("snack:food_edit", args=[self.food.id]))
    self.assertNotEqual(response.status_code, 200)
  
  def test_authenticated_staff_user_can_edit_food(self):
    self.client.force_login(user=self.staff_user)
    response = self.client.get(reverse("snack:food_edit", args=[self.food.id]))
    self.assertEqual(response.status_code, 200)

  # def test_authenticated_staff_user_can_edit_food_with_valid_inputs(self):
  #   self.client.force_login(user=self.staff_user)  
  #   response = self.client.post("/snack/list/" + str(self.food.id) + "/edit/", {'inventory': 20})
  #   self.assertContains(response, '<li class="success">')
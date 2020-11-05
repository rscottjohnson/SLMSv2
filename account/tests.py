from django.test import LiveServerTestCase
from selenium import webdriver
from django.http.request import HttpRequest
from django.urls import resolve
from django.test import TestCase
from account.views import dashboard

# Create your tests here.

class LoginPageTest(TestCase):

  def test_root_url_resolves_to_dashboard_view(self):
    found = resolve('/')
    self.assertEqual(found.func, dashboard)

from django.test import TestCase
from django.urls import resolve, reverse


class TestURL(TestCase):
    def setUp(self):
        self.client.login(username="admin", password="password")

    def test_url_resolved(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.get(reverse("task_management:boardlist_view"))
        print(response.func)
        self.assertEqual(response.status_code, 200)

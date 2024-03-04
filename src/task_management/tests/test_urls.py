from django.test import TestCase
from django.urls import resolve, reverse


class TestURL(TestCase):
    def setUp(self):
        self.client.login(username="admin", password="password")

    def test_url_resolved(self):
        response = self.client.get(reverse("task_management:boardlist_view"))
        self.assertEqual(response.status_code, 200)

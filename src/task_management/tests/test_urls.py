from django.test import TestCase
from django.urls import resolve, reverse


class TestURL(TestCase):
    def test_url_resolved(self):

        print(resolve("task_management:boardlist_view"))
        assert 1 == 1

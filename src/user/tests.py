from json import load
from os.path import join

from django.conf import settings
from django.test import TestCase
from django.urls import reverse

from abstract.utils import count_json_obj
from user.models import User


class TestModel(TestCase):
    fixtures = ["user.json"]

    def setUp(self):
        with open(join(settings.FIXTURE_DIRS[0], self.fixtures[0]), "r") as tmp_file:
            self.json_data = load(tmp_file)

    def test_user(self):
        self.assertEqual(
            User.objects.all().count(),
            count_json_obj(self.json_data, str(User._meta)),
        )

    def tearDown(self):
        User.objects.all().delete()


class TestUrl(TestCase):
    fixtures = ["user.json"]

    def setUp(self):
        with open(join(settings.FIXTURE_DIRS[0], self.fixtures[0]), "r") as tmp_file:
            self.json_data = load(tmp_file)

    def test_dashboard(self):
        self.client.login(
            username=self.json_data[0]["fields"]["username"], password="password"
        )
        response = self.client.get(reverse("user:dashboard_view"))
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.get(reverse("user:login_view"))
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        self.client.login(
            username=self.json_data[0]["fields"]["username"], password="password"
        )
        response = self.client.post(reverse("user:logout_view"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("user:login_view"), status_code=302)

    def test_registration(self):
        response = self.client.get(reverse("user:registration_view"))
        self.assertEqual(response.status_code, 200)

    def test_healthcheck(self):
        response = self.client.get(reverse("user:healthcheck_view"))
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        User.objects.all().delete()

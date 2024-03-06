from json import load
from os.path import join

from django.conf import settings
from django.test import TestCase
from django.urls import reverse

from abstract.utils import count_json_obj, generate_str
from task_management.models import Board, List, Task
from user.models import User


class TestModel(TestCase):
    fixtures = ["user.json", "task_management.json"]

    def setUp(self):
        with open(join(settings.FIXTURE_DIRS[0], self.fixtures[1]), "r") as tmp_file:
            self.task_json = load(tmp_file)

    def test_board(self):
        self.assertEqual(
            Board.objects.all().count(),
            count_json_obj(self.task_json, str(Board._meta)),
        )

    def test_list(self):
        self.assertEqual(
            List.objects.all().count(),
            count_json_obj(self.task_json, str(List._meta)),
        )

    def test_tasks(self):
        self.assertEqual(
            Task.objects.all().count(),
            count_json_obj(self.task_json, str(Task._meta)),
        )

    def tearDown(self):
        Board.objects.all().delete()
        List.objects.all().delete()
        Task.objects.all().delete()
        User.objects.all().delete()


class TestUrl(TestCase):
    fixtures = ["user.json", "task_management.json"]

    def setUp(self):
        with open(join(settings.FIXTURE_DIRS[0], self.fixtures[0]), "r") as tmp_file:
            self.user_json = load(tmp_file)
        with open(join(settings.FIXTURE_DIRS[0], self.fixtures[1]), "r") as tmp_file:
            self.task_json = load(tmp_file)
        self.client.login(
            username=self.user_json[0]["fields"]["username"], password="password"
        )

    def test_boardlist(self):
        response = self.client.get(reverse("task_management:boardlist_view"))
        self.assertEqual(response.status_code, 200)

    def test_boardcreate(self):
        tmp_form = {"name": generate_str(8)}
        response = self.client.post(
            reverse("task_management:boardcreate_view"), data=tmp_form
        )
        self.assertEqual(response.status_code, 200)

import os
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

    def test_board(self):
        response = self.client.get(reverse("task_management:boardlist_view"))
        self.assertEqual(response.status_code, 200)
        tmp_form = {"name": generate_str()}
        response = self.client.post(
            reverse("task_management:boardcreate_view"), data=tmp_form
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            Board.objects.count(), count_json_obj(self.task_json, str(Board._meta)) + 1
        )
        tmp_object = Board.objects.last()
        self.assertEqual(tmp_object.name, tmp_form["name"])
        tmp_form = {"name": generate_str()}
        response = self.client.post(
            reverse("task_management:boardupdate_view", kwargs={"pk": tmp_object.pk}),
            data=tmp_form,
        )
        self.assertEqual(response.status_code, 302)
        tmp_object = Board.objects.last()
        self.assertEqual(tmp_object.name, tmp_form["name"])

        tmp_child_form = {"name": generate_str()}
        response = self.client.post(
            reverse(
                "task_management:boardlistcreate_view", kwargs={"pk": tmp_object.pk}
            ),
            data=tmp_child_form,
        )
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            reverse("task_management:boarddelete_view", kwargs={"pk": tmp_object.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            Board.objects.count(), count_json_obj(self.task_json, str(Board._meta))
        )

    def test_list(self):
        response = self.client.get(reverse("task_management:listlist_view"))
        self.assertEqual(response.status_code, 200)
        tmp_form = {"name": generate_str()}
        response = self.client.post(
            reverse("task_management:listcreate_view"), data=tmp_form
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            List.objects.count(), count_json_obj(self.task_json, str(List._meta)) + 1
        )
        tmp_object = List.objects.last()
        self.assertEqual(tmp_object.name, tmp_form["name"])
        tmp_form = {"name": generate_str()}
        response = self.client.post(
            reverse("task_management:listupdate_view", kwargs={"pk": tmp_object.pk}),
            data=tmp_form,
        )
        self.assertEqual(response.status_code, 302)
        tmp_object = List.objects.last()
        self.assertEqual(tmp_object.name, tmp_form["name"])

        tmp_child_form = {"name": generate_str()}
        response = self.client.post(
            reverse(
                "task_management:listtaskcreate_view", kwargs={"pk": tmp_object.pk}
            ),
            data=tmp_child_form,
        )
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            reverse("task_management:listdelete_view", kwargs={"pk": tmp_object.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            List.objects.count(), count_json_obj(self.task_json, str(List._meta))
        )

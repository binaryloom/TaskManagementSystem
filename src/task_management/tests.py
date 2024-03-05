from json import load
from os.path import join

from django.conf import settings
from django.test import TestCase

from task_management.models import Board, List, Task
from user.models import User


class TestModel(TestCase):
    fixtures = ["user.json", "task_management.json"]

    def setUp(self):
        self.boards = Board.objects.all()
        self.lists = List.objects.all()
        self.tasks = Task.objects.all()
        with open(join(settings.FIXTURE_DIRS[0], self.fixtures[1]), "r") as tmp_file:
            self.json_data = load(tmp_file)

    def test_board(self):
        print(self.json_data)
        self.assertEqual(self.boards.count(), 1)

    def test_list(self):
        self.assertEqual(self.lists.count(), 2)

    def test_tasks(self):
        self.assertEqual(self.tasks.count(), 3)

    def tearDown(self):
        Board.objects.all().delete()
        List.objects.all().delete()
        Task.objects.all().delete()
        User.objects.all().delete()

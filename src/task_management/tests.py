from django.test import TestCase

from task_management.models import Board, List, Task


class TestModel(TestCase):
    fixtures = ["user.json", "task_management.json"]

    def setUp(self):
        self.boards = Board.objects.all()
        self.lists = List.objects.all()
        self.tasks = Task.objects.all()

    def test_board(self):
        self.assertEqual(self.boards.count(), 1)

    def test_list(self):
        self.assertEqual(self.lists.count(), 2)

    def test_tasks(self):
        self.assertEqual(self.tasks.count(), 3)

    # def setUp(self):
    #     self.obj = Board.objects.get(pk=1)

    # def test_fixture_data_usage(self):
    #     self.assertEqual(self.obj.name, "board")

    # def tearDown(self):
    #     self.obj.delete()


# class TestModel(TestCase):
#     def setUp(self):
#         return super().setUp()

#     def test_obj(self):
#         assert 1 == 1

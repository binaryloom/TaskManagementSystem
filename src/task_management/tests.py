from django.test import TestCase

from task_management.models import Board, List, Task


class TestModel(TestCase):
    fixtures = ["user.json", "task_management.json"]

    def setUp(self):
        self.boards = Board.objects.all()
        self.lists = Board.objects.all()
        self.tasks = Board.objects.all()

    def test_board(self):
        self.assertEqual(self.board.name, "board")

    def test_list(self):
        self.assertEqual(self.board.name, "board")

    def test_tasks(self):
        self.assertEqual(self.board.name, "board")

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

from django.test import TestCase

from task_management.models import Board, List, Task


class MyTestCase(TestCase):
    fixtures = ["myapp_fixture.json"]

    def setUp(self):
        # Load data from the fixture into test case
        self.obj = MyModel.objects.get(pk=1)

    def test_fixture_data_usage(self):
        # Use the loaded data for testing
        self.assertEqual(self.obj.name, "Test")

    # Add more test methods as needed

    def tearDown(self):
        # Remove the data after the test is executed
        self.obj.delete()


# class TestModel(TestCase):
#     def setUp(self):
#         return super().setUp()

#     def test_obj(self):
#         assert 1 == 1

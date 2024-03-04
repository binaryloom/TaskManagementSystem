from django.test import TestCase


class TestModel(TestCase):
    def setUp(self):
        return super().setUp()

    def test_obj(self):
        assert 1 == 1

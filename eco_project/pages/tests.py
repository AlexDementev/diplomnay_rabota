from django.test import TestCase

from pages.models import Product, MyUser


class Test1(TestCase):

    @classmethod
    def setUpTestData(cls):
        MyUser.objects.create(username="test", password="test")

    def setUp(self):
        pass

    def test_1(self):
        print("Method: test_1")
        user = MyUser.objects.get(username="test")
        self.assertEquals(user.username, 'test')

    def test_2(self):
        print("Method: test_2")
        try:
            # ошибка при дублировании username
            MyUser.objects.create(username="test", password="test")
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_3(self):
        print("Method: test_3")
        try:
            # ошибка при дублировании username
            MyUser.objects.create(username="test3", password="*SDF" * 2555)
            self.assertTrue(False)
        except:
            self.assertTrue(True)

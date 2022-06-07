from unittest import TestCase

from src.inmdb import InMDB


class TestData(TestCase):

    def setUp(self) -> None:
        self.db = InMDB()

    def test_set_get(self):
        var = "X"
        value = 10
        self.db.set(var, value)
        result = self.db.get(var)
        self.assertEqual(value, result)
        self.db.unset(var)
        result = self.db.get(var)
        self.assertEqual(None, result)

    def test_numequalto(self):
        self.db.set("a", 10)
        self.db.set("b", 10)

        result = self.db.numequalto(10)
        self.assertEqual(2, result)

        result = self.db.numequalto(20)
        self.assertEqual(0, result)

        self.db.set("b", 30)

        result = self.db.numequalto(10)
        self.assertEqual(1, result)





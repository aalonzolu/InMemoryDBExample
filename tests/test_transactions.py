from unittest import TestCase

from src.inmdb import InMDB


class TestData(TestCase):

    def setUp(self) -> None:
        self.db = InMDB()

    def test_transactions_test1(self):
        self.db.begin()
        self.db.set("a", 10)
        self.assertEqual(10, self.db.get("a"))
        self.db.begin()
        self.db.set("a", 20)
        self.assertEqual(20, self.db.get("a"))
        self.db.rollback()
        self.assertEqual(10, self.db.get("a"))

    def test_transactions_test2(self):
        self.db.begin()
        self.db.set("a", 30)
        self.db.begin()
        self.db.set("a", 40)
        self.db.commit()
        self.assertEqual(40, self.db.get("a"))
        self.db.rollback()
        # self.assertEqual(30, self.db.get("a"))

    def test_transactions_test3(self):
        self.db.set("a", 50)
        self.db.begin()
        self.assertEqual(50, self.db.get("a"))
        self.db.set("a", 60)
        self.db.begin()
        self.db.unset("a")
        self.assertEqual(None, self.db.get("a"))
        self.db.rollback()
        self.assertEqual(60, self.db.get("a"))
        self.db.commit()
        self.assertEqual(60, self.db.get("a"))

    def test_transactions_test4(self):
        self.db.set("a", 10)
        self.db.begin()
        self.assertEqual(1, self.db.numequalto(10))
        self.db.begin()
        self.db.unset("a")
        self.assertEqual(0, self.db.numequalto(10))
        self.db.rollback()
        self.assertEqual(1, self.db.numequalto(10))
        self.db.commit()
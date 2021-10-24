import unittest

from ..customlist import CustomList


class TestCustomListAdd(unittest.TestCase):
    def setUp(self) -> None:
        self.left_custom_list = CustomList([1, 2])
        self.right_custom_list = CustomList([3, 0, -1.5])

    def test_is_custom_list(self):
        self.assertIsInstance(self.left_custom_list
                              + self.right_custom_list, CustomList)
        self.assertIsInstance(self.right_custom_list
                              + self.left_custom_list, CustomList)
        self.assertIsInstance(self.left_custom_list + [], CustomList)
        self.assertIsInstance([] + self.right_custom_list, CustomList)

    def test_add(self):
        res_list = CustomList([4, 2, -1.5])
        self.assertListEqual(self.left_custom_list
                             + self.right_custom_list, res_list)
        self.assertListEqual(self.left_custom_list + [3, 0, -1.5], res_list)

    def test_radd(self):
        res_list = CustomList([4, 2, -1.5])
        self.assertListEqual([1, 2] + self.right_custom_list, res_list)


class TestCustomListSub(unittest.TestCase):
    def setUp(self) -> None:
        self.left_custom_list = CustomList([1, 2])
        self.right_custom_list = CustomList([3, 0, -1.5])

    def test_is_custom_list(self):
        self.assertIsInstance(self.left_custom_list
                              - self.right_custom_list, CustomList)
        self.assertIsInstance(self.right_custom_list
                              - self.left_custom_list, CustomList)
        self.assertIsInstance(self.left_custom_list - [], CustomList)
        self.assertIsInstance([] - self.right_custom_list, CustomList)

    def test_sub(self):
        res_list = CustomList([-2, 2, 1.5])
        self.assertListEqual(self.left_custom_list
                             - self.right_custom_list, res_list)
        self.assertListEqual(self.left_custom_list - [3, 0, -1.5], res_list)

    def test_rsub(self):
        res_list = CustomList([-2, 2, 1.5])
        self.assertListEqual([1, 2] - self.right_custom_list, res_list)


class TestCustomListEq(unittest.TestCase):
    def setUp(self) -> None:
        self.left_custom_list = CustomList([1, 2])
        self.right_custom_list = CustomList([1, 2])
        self.default_list_eq = [1, 2]
        self.default_list_not_eq = [3, 4]

    def test_eq(self):
        self.assertTrue(self.left_custom_list == self.right_custom_list)
        self.assertTrue(self.left_custom_list == self.default_list_eq)
        self.assertTrue(self.default_list_eq == self.right_custom_list)
        self.assertFalse(self.default_list_not_eq == self.right_custom_list)
        self.assertFalse(self.left_custom_list == self.default_list_not_eq)

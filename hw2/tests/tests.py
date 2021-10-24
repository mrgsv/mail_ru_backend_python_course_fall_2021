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
        self.assertListEqual(self.left_custom_list + [], self.left_custom_list)

    def test_radd(self):
        res_list = CustomList([4, 2, -1.5])
        self.assertListEqual([1, 2] + self.right_custom_list, res_list)
        self.assertListEqual([] + self.right_custom_list,
                             self.right_custom_list)


class TestCustomListSub(unittest.TestCase):
    def setUp(self) -> None:
        self.left_custom_list = CustomList([1, 2])
        self.right_custom_list = CustomList([3, 0, -1.5])

    def test_is_custom_list(self):
        self.assertIsInstance(self.left_custom_list
                              - self.right_custom_list, CustomList)
        self.assertIsInstance(self.right_custom_list
                              - self.left_custom_list, CustomList)
        self.assertIsInstance(self.left_custom_list - [1, 2], CustomList)
        self.assertIsInstance(self.left_custom_list - [], CustomList)
        self.assertIsInstance([] - self.right_custom_list, CustomList)
        self.assertIsInstance([1, 2] - self.right_custom_list, CustomList)

    def test_sub(self):
        res_list = CustomList([-2, 2, 1.5])
        self.assertListEqual(self.left_custom_list
                             - self.right_custom_list, res_list)
        self.assertListEqual(self.left_custom_list - [3, 0, -1.5], res_list)
        self.assertListEqual(self.left_custom_list - [], self.left_custom_list)

    def test_rsub(self):
        res_list = CustomList([-2, 2, 1.5])
        self.assertListEqual([1, 2] - self.right_custom_list, res_list)
        self.assertListEqual([] - self.right_custom_list,
                             CustomList([-x for x in self.right_custom_list]))


class TestCustomListEq(unittest.TestCase):
    def setUp(self) -> None:
        self.left_custom_list = CustomList([1, 2])
        self.right_custom_list = CustomList([1, 2])
        self.default_list_eq = [1, 2]
        self.default_list_not_eq = [3, 4]

    def test_eq_returns_bool(self):
        self.assertIsInstance(self.left_custom_list
                              == self.right_custom_list, bool)
        self.assertIsInstance(self.default_list_eq
                              == self.right_custom_list, bool)
        self.assertIsInstance(self.default_list_not_eq
                              == self.right_custom_list, bool)

    def test_eq_lists(self):
        self.assertTrue(self.left_custom_list == self.right_custom_list)
        self.assertTrue(self.left_custom_list == self.default_list_eq)
        self.assertFalse(self.left_custom_list == self.default_list_not_eq)

    def test_eq_raises_assert_if_not_list(self):
        with self.assertRaises(AssertionError):
            self.left_custom_list == 1


if __name__ == '__main__':
    unittest.main()

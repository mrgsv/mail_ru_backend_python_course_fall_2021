import unittest

from ..custommeta import CustomMeta


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100


class TestCustomMeta(unittest.TestCase):
    def setUp(self) -> None:
        self.custom_obj = CustomClass()

    def test_attr_renamed(self):
        self.assertEqual(self.custom_obj.custom_x, 50)
        self.assertEqual(self.custom_obj.custom_val, 99)

    def test_attr_raises_attr_exception(self):
        with self.assertRaises(AttributeError):
            _ = self.custom_obj.x
        with self.assertRaises(AttributeError):
            _ = self.custom_obj.val

    def test_method_renamed(self):
        self.assertEqual(self.custom_obj.custom_line(), 100)

    def test_method_raises_attr_exception(self):
        with self.assertRaises(AttributeError):
            _ = self.custom_obj.line()

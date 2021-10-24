"""Module with CustomList"""


class CustomList(list):
    """Implementation of list with numpy-like operations"""
    def __init__(self, iterable_data):
        super().__init__(iterable_data)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __add__(self, other):
        return self._custom_add(other)

    def __radd__(self, other):
        return self._custom_add(other)

    def _custom_add(self, other):
        assert isinstance(other, list), (
            f"Expected list or inherited list obj, but got {type(other)}"
        )
        res = []
        if len(self) > len(other):
            for idx in range(len(other)):
                res.append(self[idx] + other[idx])
            res.extend(self[len(other):])
        else:
            for idx in range(len(self)):
                res.append(self[idx] + other[idx])
            res.extend(other[len(self):])
        return CustomList(res)

    def __sub__(self, other):
        assert isinstance(other, list), (
            f"Expected list or inherited list obj, but got {type(other)}"
        )
        res = []
        if len(self) > len(other):
            for idx in range(len(other)):
                res.append(self[idx] - other[idx])
            res.extend(self[len(other):])
        else:
            for idx in range(len(self)):
                res.append(self[idx] - other[idx])
            for el in other[len(self):]:
                res.append(-el)
        return CustomList(res)

    def __rsub__(self, other):
        assert isinstance(other, list), (
            f"Expected list or inherited list obj, but got {type(other)}"
        )
        res = []
        if len(self) > len(other):
            for idx in range(len(other)):
                res.append(other[idx] - self[idx])
            for el in self[len(other):]:
                res.append(-el)
        else:
            for idx in range(len(self)):
                res.append(other[idx] - self[idx])
            res.extend(other[len(self):])
        return CustomList(res)

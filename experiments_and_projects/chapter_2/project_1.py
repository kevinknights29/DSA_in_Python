# To the Array class in the data_structures/array.py file, add a method called
# get_max_num() that returns the maximum number in the array, or None if the array
# has no numbers. You can use the expression isinstance(value, (int, float)) to
# test for numbers.
"""Array data structure implementation."""
from __future__ import annotations


class Array:
    def __init__(self, initial_size) -> None:
        self.__arr = [None] * initial_size
        self.__n_items = 0

    def __len__(self):
        return self.__n_items

    def __str__(self) -> str:
        arr_str = ",".join([str(self.__arr[i]) for i in range(self.__n_items)])
        return f"[{arr_str}]"

    # retrieval
    def get(self, index):
        if index < 0 or index >= self.__n_items:
            raise IndexError("Index out of bounds")
        return self.__arr[index]

    # update
    def set(self, index, value):
        if index < 0 or index >= self.__n_items:
            raise IndexError("Index out of bounds")
        self.__arr[index] = value

    # insertion
    def insert(self, value):
        if self.__n_items == len(self.__arr):
            raise IndexError("Array is full")
        self.__arr[self.__n_items] = value
        self.__n_items += 1

    # find
    def find(self, value):
        for i in range(self.__n_items):
            if self.__arr[i] == value:
                return i
        return -1

    # search
    def search(self, value):
        self.get(self.find(value))

    # deletion
    def delete(self, value):
        index = self.find(value)
        if index == -1:
            raise ValueError("Value not found")
        for i in range(index, self.__n_items - 1):
            self.__arr[i] = self.__arr[i + 1]
        self.__n_items -= 1
        self.__arr[self.__n_items] = None

    # traversal
    def traverse(self, function=print):
        for i in range(self.__n_items):
            function(self.__arr[i])

    # get_max_num
    def get_max_num(self):
        max_num = None
        for i in range(self.__n_items):
            if isinstance(self.__arr[i], (int, float)):
                if max_num is None or self.__arr[i] > max_num:
                    max_num = self.__arr[i]
        return max_num


# Evaluation
if __name__ == "__main__":
    # test get_max_num
    arr_1 = Array(3)
    arr_1.insert(1)
    arr_1.insert(2)
    arr_1.insert(3)
    print(arr_1.get_max_num())  # 3
    assert arr_1.get_max_num() == 3

    # test get_max_num with no numbers
    arr_2 = Array(3)
    arr_2.insert("a")
    arr_2.insert("b")
    arr_2.insert("c")
    print(arr_2.get_max_num())  # None
    assert arr_2.get_max_num() is None

    # test get_max_num with characters and numbers
    arr_3 = Array(3)
    arr_3.insert("a")
    arr_3.insert(1)
    arr_3.insert("c")
    print(arr_3.get_max_num())  # 1
    assert arr_3.get_max_num() == 1

    print("Passed all tests!")

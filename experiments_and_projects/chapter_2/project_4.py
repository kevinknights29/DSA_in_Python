# Write a remove_duplicates() method for the Array class in
# the data_structures/array.py file, that removes any duplicate
# entries in the array.
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

    # remove_duplicates
    def remove_duplicates(self):
        dedup_arr = set(self.__arr)
        self.__arr = [None] * self.__n_items
        self.__n_items = 0
        for value in dedup_arr:
            self.insert(value)


# Evaluation
if __name__ == "__main__":
    # test get_max_num
    arr_1 = Array(3)
    arr_1.insert(1)
    arr_1.insert(1)
    arr_1.insert(3)
    arr_1.remove_duplicates()  # drop a 1
    assert len(arr_1) == 2

    # test get_max_num with no numbers
    arr_2 = Array(3)
    arr_2.insert("a")
    arr_2.insert("b")
    arr_2.insert("c")
    arr_2.remove_duplicates()  # No change
    assert len(arr_2) == 3

    # test get_max_num with characters and numbers
    arr_3 = Array(3)
    arr_3.insert("a")
    arr_3.insert("a")
    arr_3.insert("a")
    arr_3.remove_duplicates()  # drop two a's
    assert len(arr_3) == 1

    print("Passed all tests!")

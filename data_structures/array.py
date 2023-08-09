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

"""Order record array data structure implementation"""
from __future__ import annotations


def identify(x):
    return x


class OrderedRecordArray:
    def __init__(self, initial_size, key=identify):
        self.__arr = [None] * initial_size
        self.__n_items = 0
        self.__key = key

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

    # insertion
    def insert(self, value):
        if self.__n_items == len(self.__arr):
            raise IndexError("Array is full")

        index = self.find(self.__key(value))
        for i in range(self.__n_items, index, -1):
            self.__arr[i] = self.__arr[i - 1]

        self.__arr[index] = value
        self.__n_items += 1

    # find
    def find(self, key):
        low = 0
        high = self.__n_items - 1
        while low <= high:
            mid = (low + high) // 2
            if self.__key(self.__arr[mid]) == key:
                return mid
            elif self.__key(self.__arr[mid]) > key:
                high = mid - 1
            else:
                low = mid + 1
        return low

    # search
    def search(self, key):
        index = self.find(key)
        if index < self.__n_items and self.__key(self.__arr[index]) == key:
            return self.get(index)

    # deletion
    def delete(self, value):
        index = self.find(self.__key(value))
        if index < self.__n_items and self.__arr[index] != value:
            raise ValueError("Value not found")
        for i in range(index, self.__n_items - 1):
            self.__arr[i] = self.__arr[i + 1]
        self.__n_items -= 1
        self.__arr[self.__n_items] = None

    # traversal
    def traverse(self, function=print):
        for i in range(self.__n_items):
            function(self.__arr[i])

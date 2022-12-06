import random


class RandomQueue:

    def __init__(self, size=10):
        self.items = []
        self.size = size

    def insert(self, item):   # insert element in O(1)
        if self.is_full():
            raise ValueError("Queue is full")
        else:
            self.items.append(item)

    def remove(self):  # return random element in O(1)
        if self.is_empty():
            raise ValueError("Queue is empty")
        else:
            return self.items.pop(random.randint(0, len(self.items) - 1))

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.size

    def clear(self):  # clear the queue
        self.items = []

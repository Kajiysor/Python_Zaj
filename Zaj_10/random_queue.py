import random


class RandomQueue:
    def __init__(self, size=10):
        self.size = size
        self.queue = []

    def insert(self, element):
        if self.is_full():
            raise ValueError("Queue is full")

        self.queue.append(element)

    def remove(self):
        if self.is_empty():
            raise ValueError("Queue is empty")

        # Select a random element from the queue
        index = random.randint(0, len(self.queue) - 1)

        # Swap the selected element with the last element in the queue
        self.queue[index], self.queue[-1] = self.queue[-1], self.queue[index]

        # Remove the last element from the queue
        return self.queue.pop()

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.size

    def clear(self):
        self.queue = []

from LinkedList import *
class EmptyError(Exception):
    """class create to throw an exception on remove method"""
    pass


class Queue:
    def __init__(self) -> None:
        self.queue = LinkedList()

    def __repr__(self) -> str:
        return f"{self.queue}"

    def addFirst(self, value):
        self.queue.addFirst(value)

    def removeFirst(self):
        self.queue.removeFirst()

    def first(self):
        return self.queue.first()

    def size(self):
        return self.queue.__len__

    def isEmpty(self):
        return self.queue.isEmpty()

    def clear(self):
       self.queue.reset()
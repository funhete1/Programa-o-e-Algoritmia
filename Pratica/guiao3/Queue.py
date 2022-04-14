class EmptyError(Exception):
    """class create to throw an exception on remove method"""
    pass


class Queue:
    def __init__(self) -> None:
        self.queue = []

    def __repr__(self) -> str:
        return f"{self.queue}"

    def add(self, value):
        self.queue.append(value)

    def remove(self):
        try:
            self.queue.remove(self.queue[0])
        except EmptyError:
            print("the list is empty cannot remove any element")

    def first(self):
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return True if Queue.size(self) == 0 else False 

    def clear(self):
        self.queue = []
class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = []

    def enqueue(self, item):
        self.storage.insert(0, item)
        self.size += 1
        return item

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.pop()

    def len(self):
        return self.size

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, items):
        self.items.insert(0, items)

    def dequeue(self):
        if (len(self.items) == 0):
            return
        print('Dequeue: ', self.items.pop())

    def peek(self):
        print('Peek', self.items[0])

    def size(self):
        print('Size', len(self.items))


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.size()
q.dequeue()
q.dequeue()
q.dequeue()
q.size()
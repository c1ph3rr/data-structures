class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def push(self, items):
        self.items.append(items)

    def pop(self):
        print('Pop: ', self.items.pop())

    def peek(self):
        print('Peek: ', self.items[-1])

    def size(self):
        print('Size: ', len(self.items))

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.size()
s.pop()
s.size()
s.peek()
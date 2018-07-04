class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def insertNew(self, newValue):
        self.value = newValue

    def nextNew(self, newNext):
        self.next = newNext

    def displayValue(self):
        return self.value

    def displayNext(self):
        return self.next


class List():
    def __init__(self):
        self.head = None        

    def add(self, item):
        tmp = Node(item)
        tmp.nextNew(self.head)
        self.head = tmp

    def size(self):
        curr = self.head
        count = 0
        while curr != None:
            count += 1
            curr = curr.displayNext()            
            
        print(count)

    def search(self, item):
        curr = self.head
        found = False
        while curr != None and not found:
            if curr.displayValue() == item:
                found = True
            else:
                curr = curr.displayNext()

        print(found)

    def remove(self, item):
        if (self.head == None):
            return
        curr = self.head
        previous = None
        found = False
        while not found:
            if curr.displayValue() == item:
                found =True
            else:
                previous = curr
                curr = curr.displayNext()

        if previous == None:
            self.head = curr.displayNext()
        else:
            previous.nextNew(curr.displayNext())
        
    

l = List()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.add(5)
l.size()
l.search(4)
l.remove(5)
l.size()
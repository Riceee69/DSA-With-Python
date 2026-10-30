class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self):
        self._first = None
        self._last = None
        self._length = 0

    def peek(self):
        return self._first

    def enqueue(self, value):
        if(not self._length):
            self._first = self._last = Node(value)
        else:
            self._last.next = Node(value)
            self._last = self._last.next
        self._length += 1

    def dequeue(self):
        if self._last == None:
            raise IndexError("Queue Empty")
        elif self._first == self._last:
            self._first = self._last = None
        else:            
            self._first = self._first.next
        self._length -= 1

    def isEmpty(self):
        return self._last is None
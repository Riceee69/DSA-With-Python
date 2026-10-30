class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self._top = None
        self._bottom = None
        self._length = 0

    def peek(self):
        return self._top

    def push(self, value):
        if(not self._length):
            self._top = self._bottom = Node(value)
        else:
            new_node = Node(value)   
            new_node.next = self._top
            self._top = new_node
        self._length += 1

    def pop(self):
        if self._bottom == None:
            raise IndexError("Stack Empty")
        elif self._bottom == self._top:
            self._top = self._bottom = None
        else:            
            self._top = self._top.next
        self._length -= 1

    def isEmpty(self):
        return self._bottom is None

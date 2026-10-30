class ListNode:
    def __init__(self, value=0, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous

class DoubleLinkedList():

    def __init__(self, value):
        self._head = ListNode(value)
        self._tail = self._head
        self._length = 1

    def append(self, value):
        new_node = ListNode(value, None, self._tail)
        self._tail.next = new_node
        self._tail = new_node
        self._length += 1

    def prepend(self, value):
        self._head = ListNode(value, self._head, None)
        self._head.next.previous = self._head
        self._length += 1

    def insert(self, index, value):
        if(index > self._length or index < 0): raise IndexError

        if index == 0: 
            self.prepend(value) 
            return
        if index == self._length:
            self.append(value)
            return
        
        new_node = ListNode(value)
        # Traverse to target index - 1 ie the previous node of the target index
        beforeTarget_node = self._traverseIndex(index - 1)
        afterTarget_node = beforeTarget_node.next
        # insert the new node
        new_node.next = afterTarget_node
        new_node.previous = beforeTarget_node
        beforeTarget_node.next = new_node
        afterTarget_node.previous = new_node
        self._length += 1
    
    def remove(self, index):
        if(index >= self._length or index < 0): raise IndexError

        if index == 0: 
            self._head = self._head.next
            self._head.previous = None
            self._length -= 1
            return
        if index == self._length -1:
            self._tail = self._tail.previous
            self._tail.next = None
            self._length -= 1
            return

        beforeTarget_node = self._traverseIndex(index - 1)
        delete_node = beforeTarget_node.next
        afterTarget_node = delete_node.next
        beforeTarget_node.next = afterTarget_node
        afterTarget_node.previous = beforeTarget_node
        self._length -= 1
        del delete_node
        

    def _traverseIndex(self, to_node):
        last_index = self._length - 1
        diff = last_index - to_node
        # From Tail Traversal
        if to_node > diff:
            current_node = self._tail
            for _ in range(diff): 
                current_node = current_node.previous
        else:
            current_node = self._head
            for _ in range(to_node): 
                current_node = current_node.next
        return current_node

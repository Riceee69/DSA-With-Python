class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList():

    def __init__(self, value):
        self._head = ListNode(value)
        self._tail = self._head
        self._length = 1

    def append(self, value):
        new_node = ListNode(value)
        self._tail.next = new_node
        self._tail = new_node
        self._length += 1

    def prepend(self, value):
        self._head = ListNode(value, self._head)
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
        # insert the new node
        new_node.next = beforeTarget_node.next
        beforeTarget_node.next = new_node
        self._length += 1
    

    def remove(self, index):
        if(index >= self._length or index < 0): raise IndexError

        if index == 0: 
            self._head = self._head.next
            self._length -= 1
            return

        beforeTarget_node = self._traverseIndex(index - 1)
        if index == self._length - 1:
            del self._tail
            self._tail = beforeTarget_node
            self._tail.next = None
        else: 
            delete_node = beforeTarget_node.next
            beforeTarget_node.next= delete_node.next
            del delete_node
        self._length -= 1
        

    def reverse(self):

        if(self._head.next == None):
            return

        self._tail = self._head
        previous_node = None
        current_node = self._head
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self._head = previous_node        


    def _traverseIndex(self, to_node):
        current_node = self._head
        for _ in range(to_node): 
            current_node = current_node.next
        return current_node
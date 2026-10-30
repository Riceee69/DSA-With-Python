class Stack:
    def __init__(self):
        self._stack = []

    def peek(self):
        return self._stack[len(self._stack) - 1]

    def push(self, value):
        self._stack.append(value)

    def pop(self):
        return self._stack.pop()

    def isEmpty(self):
        return self._stack.__len__() == 0


# MaxHeap
class BinaryHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        index = len(self.heap) - 1

        while index > 0:
            parent = (index - 1) // 2
            if self.heap[parent] >= self.heap[index]:
                break
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent

    def extract_max(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()
        
        max = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.max_heapify(0)
        return max

    def max_heapify(self, parent_index):
        heap_size = len(self.heap)
        left = 2 * parent_index + 1
        right = left + 1
        largest = parent_index

        if left < heap_size and self.heap[left] > self.heap[largest]:
            largest = left
        if right < heap_size and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != parent_index:
            self.heap[parent_index], self.heap[largest] = self.heap[largest], self.heap[parent_index]
            self.max_heapify(largest)

    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]


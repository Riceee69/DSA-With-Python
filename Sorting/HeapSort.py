def max_heapify(A, heap_size, parent_index):
    left = 2 * parent_index + 1
    right = 2 * parent_index + 2
    largest = parent_index
    
    if left < heap_size and A[left] > A[largest]:
        largest = left
    if right < heap_size and A[right] > A[largest]:
        largest = right
    if largest != parent_index:
        A[parent_index], A[largest] = A[largest], A[parent_index]
        max_heapify(A, heap_size, largest)

def build_heap(A):
    heap_size = len(A) 
    starting_leaf_node = heap_size // 2
    # buulding the heap bottom-up
    # every index before heap_size // 2 are parents 
    for parent_index in range (starting_leaf_node - 1,-1,-1):
        max_heapify(A,heap_size, parent_index)

def heapsort(A):
    heap_size = len(A)
    build_heap(A)

    # Execute the heap sort
    for i in range(heap_size-1,0,-1):
        A[0], A[i] = A[i], A[0] 
        heap_size -= 1
        max_heapify(A, heap_size, 0)


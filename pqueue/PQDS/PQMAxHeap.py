"""
Cost of each method used in this implemetation noted in the table below:(n is the number of elements in the heap)

|--------------------|-------------------------------------------------------------------------------------------------------------------------|
\   Method           \                                                                                                                         /
|--------------------|-------------------------------------------------------------------------------------------------------------------------|
|   __init__()       | O(1) because it only involves initializing an empty list.                                                               |
|--------------------|-------------------------------------------------------------------------------------------------------------------------|
|  insert()          | O(n) in the worst case.                                                                                                 |
|                    | This is because in the worst case,                                                                                      |
|                    | it needs to extend the vector by {priority - len(self.vector) + 1} elements, which takes linear time.                   |
|                    | The enqueue operation is O(1).                                                                                          |
|--------------------|-------------------------------------------------------------------------------------------------------------------------|
|  deleteMax()       | O(log n)                                                                                                                |
|                    | because it involves removing the maximum element from the heap (which is at the root),                                  |
|                    | and then performing a heapify-down operation to maintain the heap property.                                             |
|--------------------|-------------------------------------------------------------------------------------------------------------------------|
|   findMax()        | O(1)                                                                                                                    |        
|                    | because it simply returns the element at the root of the heap, which is the maximum element                             |
|--------------------|-------------------------------------------------------------------------------------------------------------------------|
|  lookupi()         | O(1) because it simply returns the element at a given index in the heap.                                                |           
|--------------------|-------------------------------------------------------------------------------------------------------------------------|
|   heapify_up()     | O(log n) in the worst case.                                                                                             |
|                    | because it involves swapping an element with its parent until the heap property is restored                             |        
|--------------------|-------------------------------------------------------------------------------------------------------------------------|
|    heapify_down()  | O(log n) in the worst case.                                                                                             |        
|                    | because it involves swapping an element with its largest child until the heap property is restored                      |
|--------------------|-------------------------------------------------------------------------------------------------------------------------|
|   swap()           | O(1) because it simply involves swapping two elements in the heap.                                                      |            
|--------------------|-------------------------------------------------------------------------------------------------------------------------|
|  listed()          | O(n) because it involves iterating over all the elements in the heap.                                                   |
|--------------------|-------------------------------------------------------------------------------------------------------------------------|

"""



class PriorityQueue_MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, timestamp, priority):
        heap = self.heap
        heap.append((timestamp, priority))
        self._heapify_up(len(self.heap) - 1)
        

    def deleteMax(self):
        if self.heap:
            self._swap(0, len(self.heap) - 1)
            max_item = self.heap.pop()
            self._heapify_down(0)
            return max_item[0], max_item[1]

    def findMax(self):
        if self.heap:
            return self.heap[0][0], self.heap[0][1]

    def lookupi(self, index):
        int(index)
        if 0 <= index < len(self.heap):
            return self.heap[index][1]

    def reset(self):
        self.heap = []

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index][0] > self.heap[parent][0]:
            self._swap(index, parent)
            self._heapify_up(parent)

    def _heapify_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left][0] > self.heap[largest][0]:
            largest = left
        if right < len(self.heap) and self.heap[right][0] > self.heap[largest][0]:
            largest = right

        if largest != index:
            self._swap(index, largest)
            self._heapify_down(largest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def listed(self):
        for i in range(len(self.heap)):
            print(self.heap[i][0], end=" ")

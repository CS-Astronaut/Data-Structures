"""
Note: enqueue, dequeue, top and etc used in the PriorityQueue_VectorOfPQs class is defined in Queue class.

Cost of each method used in this implemetation noted in the table below:(n is the number of elements in the linked List)

|--------------------|-------------------------------------------------------------------------------------------------------------------------|
\   Method           \                                                                                                                         /
|--------------------|-------------------------------------------------------------------------------------------------------------------------|
|   __init__()       | O(1) because it only involves initializing an empty list.                                                               |
|--------------------|-------------------------------------------------------------------------------------------------------------------------|
|  insert()          | The time complexity of this method is O(n) in the worst case.                                                           |
|                    | This is because in the worst case,                                                                                      |
|                    | it needs to extend the vector by priority - len(self.vector) + 1 elements, which takes linear time.                     |
|                    | The enqueue operation is O(1).                                                                                          |
|--------------------|-------------------------------------------------------------------------------------------------------------------------|
|  deleteMax()       | O(n)                                                                                                                    |
|                    | because it iterates over all the elements in the vector to find the queue with the highest priority that is not empty.  |
|                    | The dequeue operation is O(1).                                                                                          |
|--------------------|-------------------------------------------------------------------------------------------------------------------------|
|   findMax()        | O(n)                                                                                                                    |
|                    | Same reason as deletemax() method behavior.                                                                             |
|                    | The top operation is O(1).                                                                                              |
|--------------------|-------------------------------------------------------------------------------------------------------------------------|
|  lookupi()         | O(1) because it simply returns a string.                                                                                |
|--------------------|-------------------------------------------------------------------------------------------------------------------------|
|  reset()           | O(1) because it only involves reinitializing the vector to an empty list.                                               |
|--------------------|-------------------------------------------------------------------------------------------------------------------------|
|   listed()         | O(n) because it iterates over all the elements in the vector.                                                          |
|--------------------|-------------------------------------------------------------------------------------------------------------------------|

"""



class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return "Queue is Empty!"
    
    def top(self):
        if not self.is_empty():
            return self.items[0]
        return "Queue is Empty!"       

    def is_empty(self):
        return len(self.items) == 0




class PriorityQueue_VectorOfPQs:
    def __init__(self):
        self.vector = [None]

    def insert(self, timestamp, priority):
        if priority >= len(self.vector):
            self.vector += [None] * (priority - len(self.vector) + 1)
        if self.vector[priority] is None:
            self.vector[priority] = Queue()
        self.vector[priority].enqueue(timestamp)

    def deleteMax(self):
        for queue in self.vector:
            if queue and not queue.is_empty():
                return queue.dequeue()
        return "Queue is Empty!"
    
    def findMax(self):
        for queue in self.vector:
            if queue and not queue.is_empty():
                return queue.top()
        return "Queue is Empty!"
    
    def lookupi(self, index):
        return "can't perform this task in this Data Structure."
        

    def reset(self):
        self.vector = [None]
    

    def listed(self):
        for i, queue in enumerate(self.vector):
            str(i)
            if queue:
                
                print(f"Priority {i}: {''.join(str(queue.items))}")

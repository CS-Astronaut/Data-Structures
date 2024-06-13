"""
Cost of each method used in this implemetation noted in the table below:( n is the number of elements in the heap)

|--------------------|-------------------------------------------------------------------------------------------------------------------------|
\   Method           \                                                                                                                         /
|--------------------|-------------------------------------------------------------------------------------------------------------------------|
|   __init__()       | O(1) because it only involves initializing an empty list.                                                               |
|--------------------|-------------------------------------------------------------------------------------------------------------------------|
|   isempty()        | O(1)                                                                                                                    |
|                    | because it only checks if the front of the queue is None                                                                |
|--------------------|-------------------------------------------------------------------------------------------------------------------------|
|   push()           | O(n)                                                                                                                    |
|                    | in the worst case, it needs to itarate the entire linked list to find the correct position to insert the new node.      |
|--------------------|-------------------------------------------------------------------------------------------------------------------------|
|   findMax()        | O(1)                                                                                                                    |        
|                    | because it simply returns the timestamp of the front node, which is the maximum priority node in the queue.             |
|--------------------|-------------------------------------------------------------------------------------------------------------------------|
|  lookupi()         | O(1) in the worst case, it needs to itarate the entire linked list to find the node at the given index.                 |           
|--------------------|-------------------------------------------------------------------------------------------------------------------------|
|     reset()        |  O(1) because it only involves setting the front of the queue to None                                                   |
|--------------------|-------------------------------------------------------------------------------------------------------------------------|
|  listed()          | O(n) because it involves iteratig the entire linked list to print all the timestamps.                                   |
|--------------------|-------------------------------------------------------------------------------------------------------------------------|

"""

class PriorityQueueNode: 
    def __init__(self, timestamp, pr):
        self.timestamp = timestamp
        self.priority = pr
        self.next = None

class PriorityQueue_LinkedLists: 
    def __init__(self): 
        self.front = None

    #private method
    def __isempty(self): 
        return True if self.front == None else False

    def push(self, timestamp, priority): 

        if self.__isempty() == True: 
            self.front = PriorityQueueNode(timestamp,priority)

        else: 
            if self.front.priority > priority: 
                newNode = PriorityQueueNode(timestamp,priority) 
                newNode.next = self.front 
                self.front = newNode 


            else: 
                temp = self.front 
                while temp.next:
                    if priority == temp.next.priority:

                        #If two items have the same priority, then the tie is broken by ordering the item with the smallest value (timestamp) first
                        if timestamp < temp.next.timestamp:
                            break
                        else:
                            temp = temp.next

                    elif priority < temp.next.priority: 
                        break

                    else:
                        temp = temp.next
                

                newNode = PriorityQueueNode(timestamp,priority)
                print(f"{newNode.timestamp}{temp.timestamp}")
                newNode.next = temp.next
                temp.next = newNode

    def findMax(self): 

        if self.__isempty() == True: 
            return
        else: 
            return self.front.timestamp 

    def deleteMax(self): 
        if self.__isempty() == True: 
            pass
        else: 
            temp = self.front.timestamp
            self.front = self.front.next
            return temp
        

    def listed(self): 

        if self.__isempty() == True: 
            return "Queue is Empty!"
        
        else: 
            temp = self.front 
            while temp: 
                print(temp.timestamp, end = " ") 
                temp = temp.next

    def lookupi(self, index):

        if self.__isempty() == True: 
            return "Queue is Empty!"
        
        else: 
            temp = self.front 
            i = 0
            while temp:
                if i == index:
                    return (temp.timestamp, temp.priority)
                i += 1
                temp = temp.next

    def reset(self):

        if self.__isempty() == True: 
            return "Queue is Empty!"
        
        else: 
            self.front = None



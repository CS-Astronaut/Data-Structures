# Implementation Of Priority Queue with 3 Data structures defined in the pdf using python with runtime analysis.
# By Mohammad Amin Farahani
# https://github.com/CS-astronaut 

# Check out PQDS folder to find out about implementations and thier complexities :)
from PQDS.PQLinkedList import *
from PQDS.PQMAxHeap import *
from PQDS.PQVector import *



method = input("""
Hello! Choose your desired Implementation of Priority Queues to continue...

Implementation of PQ using:
                                                         
1.Linked Lists
                   
2.Max-Heap
                   
3.A vector of queues

>>>""")

def get_command():
    command = input("""
    i : insert
    d : del and print highest priority item
    f : print highest priority item
    l : performs a lookup of the i-th item 
    r : reset PQ
    x : exit

    >>>""")
    return command

# initials
pq = PriorityQueue_LinkedLists()
pq2 = PriorityQueue_MaxHeap()
pq3 = PriorityQueue_VectorOfPQs()

timestamp = 1

# main loop 
while True:

    command = get_command()

    if command == 'x':
        break

    elif command == 'i':
        if method == '1':
            #Use PQLinkedList to insert
            priority = int(input("input priority: "))
            pq.push(timestamp, priority)
            timestamp += 1
            pq.listed()
        
        if method == '2':
            priority = int(input("input priority: "))
            pq2.insert(timestamp, priority)
            timestamp += 1
            pq2.listed()

        if method == '3':
            priority = int(input("input priority: "))
            pq3.insert(timestamp, priority)
            timestamp += 1
            pq3.listed()               


    elif command == 'd':
        if method == '1':
            #Use PQLinkedList to delete and return the highest prority item
            max = pq.deleteMax()
            print(f"The max priority item has been deleted: {max}")
            pq.listed()
        
        if method == '2':
            max = pq2.deleteMax()
            print(f"The max priority item has been deleted: {max}")
            pq2.listed()          

        if method == '3':
            max = pq3.deleteMax()
            print(f"The max priority item has been deleted: {max}")
            pq3.listed() 



    elif command == 'f':
        if method == '1':
            max = pq.findMax()
            print(f"The max priority item is: {max}")
            pq.listed()
            
        if method == '2':
            max = pq2.findMax()
            print(f"The max priority item is: {max}")
            pq2.listed()

        if method == '3':
            max = pq3.findMax()
            print(f"The max priority item is: {max}")
            pq3.listed()



    elif command == 'l':
        if method == '1':
            pq.listed()
            index = input("which index do you searching for? ")
            value = pq.lookupi(index)
            print(value)

        if method == '2':
            pq2.listed()
            index = input("which index do you searching for? ")
            value = pq2.lookupi(index)
            print(value)

        if method == '3':
            pq3.listed()
            index = input("which index do you searching for? ")
            value = pq3.lookupi(index)
            print(value)            



    elif command == 'r':

        timestamp = 1

        if method == '1':
            pq.reset()            
        if method == '2':
            pq2.reset()
        if method == '3':
            pq3.reset()

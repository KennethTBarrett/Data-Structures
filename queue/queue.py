# from singly_linked_list import LinkedList

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
#### ARRAY IMPLEMENTATION - FUNCTIONS. ####
# class Queue:
#     def __init__(self):
#         self.storage = []  # Empty array to populate.
    
#     def __len__(self):
#         # Return the length of our array.
#         return len(self.storage)

#     def enqueue(self, value):
#         """Adds item to queue"""
#         self.storage.append(value)

#     def dequeue(self):
#         """Removes item from queue"""
#         if len(self.storage) == 0:
#             return None
#         else:
#             dequeued = self.storage[0]
#             self.storage.remove(dequeued)
#             return dequeued

### LAZY WAY FOR MVP - FUNCTIONS. ####
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()
#     def __len__(self):
#         return self.size
#     def enqueue(self, value):
#         """Adds item to the tail of our queue"""
#         self.storage.add_to_tail(value)
#         self.size += 1
#     def dequeue(self):
#         """Removes the first element from our queue."""
#         if self.size == 0:
#             return None
#         else:
#             dequeued = self.storage.head.get_value()
#             self.storage.remove_head()
#             self.size -= 1
#             return dequeued

#### FROM SCRATCH - FUNCTIONS. ####
class LinkedList:
    """Class for our Linked List data structure."""
    def __init__(self):
        self.head = None
        self.tail = None

class Node:
    """This is the node class for our LinkedList."""
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        """Adds item to the tail of our queue."""
        new_node = Node(value)
        if self.storage.head is None and self.storage.tail is None:  # If there's no head/tail...
            self.storage.head = new_node  # Assign our new node as the head...
            self.storage.tail = new_node  # ... and the tail.
        else:  # Otherwise...
            # Reassign tail.
            self.storage.tail.next = new_node
            self.storage.tail = new_node
        self.size += 1  # Add 1 to the size.

    def dequeue(self):
        """Removes the first element from our queue."""
        if self.size == 0:  # If the list is empty...
            return None  # Return nothing.
        else:  # Otherwise...
            if self.storage.head is None and self.storage.tail is None:  # If there's no head/tail...
                return None  # Return none.
            if self.storage.head.next is None:  # If there's no next value after the head...
                head = self.storage.head  # Assign `head` to return.
                self.storage.head = None  # Delete head entry.
                self.storage.tail = None  # Delete tail entry.
                self.size -= 1  # Remove 1 from the size.
                return head.value
            value = self.storage.head.value  # Assign `value` to return.
            self.storage.head = self.storage.head.next  # Set the head as the next entry.
            self.size -= 1  # Remove 1 from the size.
            return value

#### ANSWER TO QUESTION 3: ####
# Linked Lists are more suited to queues than they are stacks due to memory allocation, due
# to the fact that in the use case of a queue, once the item has been removed from memory, the
# next item can take its place, granting an optimized solution.
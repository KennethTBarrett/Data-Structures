
from singly_linked_list import LinkedList, Node
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
#### ARRAY AS STORAGE STRUCTURE - FUNCTIONS. ####

# The following Stack class uses an array as the underlying storage structure.
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.value = value
#         self.storage.append(value)

#     def pop(self):
#         if self.storage:
#             return self.storage.pop()
# class LinkedList:
#     """This is the class for our LinkedList."""
#     def __init__(self):
#         self.head = None
#         self.tail = None

# class Node:
#     """This is the node class for the nodes within our linkedlist."""
#     def __init__(self, value):
#         self.value = value
#         self.next = next


#### FROM SCRATCH - DOES NOT FUNCTION (SEE NOTES). ####
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()

#     def push(self, value):
#         new_node = Node(value)  # This is our new node.
#         # First, confirm if there is a head or not.
#         if self.storage.head is None:  # If there is not...
#             self.storage.head = new_node  # Make our value the head.
#         else:  # Otherwise...
#             self.storage.next = new_node  # Make it the next value.
#         self.size += 1  # Add to the size of the linkedlist.
            
#     def pop(self):
        # # Ensure the location is our tail by looping through the linkedlist.
        # while self.storage.next is not None:  # While the next value isn't the tail
        #     self.storage.value = self.storage.next  # Set the next value to the following value.
        #     #### MY ISSUE ####
        #     # I'm having an impossible time figuring out how to set the value following the .next value...
        #     # Something along the lines of .next.next if that makes sense? I've completed MVP using the LinkedList class
        #     # given in lecture, however I would like to discuss how to make this function for better fundamental understanding.
        #     #### /END ISSUE ####
        # value = self.storage.value  # This is our tail. Using to return.
        # # Set the popped tail's value to None.
        # self.storage.next = None
        # # Set the current value as our new tail.
        # self.storage.value = self.storage.tail
        # self.size -= 1  # Subtract from the size of our linkedlist.
        
        # return value


#### LAZY METHOD FOR MVP - FUNCTIONS. ####
# class Stack:
#     def __init__(self):
#         self.size = 0  # Set the default size to zero.
#         self.storage = LinkedList()
#     def __len__(self):
#         return self.size

#     def push(self, value):
#         """This will add an item to the top of the stack, much like .append"""
#         self.storage.add_to_tail(value)
#         self.size += 1
    
#     def pop(self):
#         """This will return and remove the last item in our linkedlist."""
#         if self.size == 0:
#             return None
#         else:
#             value = self.storage.remove_tail()
#             self.size -= 1
#             return value


### Answer to Number Three: ####
# When implementing a stack via Linked List vs an array, there is a significant increase in runtime complexity.
# Because arrays support random access by index, they are faster, with a runtime complexity of O(1) to access
# an element. Because Linked Lists work off sequential access, we need to traverse the list until the desired
# element has been reached. Because of this, runtime complexity is O(n), where n is the `nth` element of the list.
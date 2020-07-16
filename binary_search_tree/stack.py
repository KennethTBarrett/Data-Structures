
"""
A stack is a data structure whose primary purpose is to store andourourour
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

class Stack:
    def __init__(self):
        self.size = 0  # Set default size to 0.
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        """Adds item to the top of the stack."""
        new_node = Node(value)
        if self.storage.head is None and self.storage.tail is None:  # If head / tail doesn't exist...
            self.storage.head = new_node  # Set the head to the new node.
            self.storage.tail = new_node  # Set the tail to the new node.
        else:  # Otherwise...
            self.storage.tail.next = new_node  # Set the tail's next item to our new node.
            self.storage.tail = new_node  # Set the tail as our new node.
        self.size += 1  # Add one to the size.
    def pop(self):
        if self.size == 0:  # If the list is empty...
            return None  # Return nothing.
        else:  # Otherwise...
            if self.storage.head is None:  # If there's no head...
                return None  # Return none.
            current = self.storage.head  # Setting `current` value to the head.
            while current.next and current.next is not self.storage.tail:  # as long as the next value exists & isn't the tail...
                current = current.next  # continue to traverse through the list.
            value = self.storage.tail.value  # `value` to return.
            self.storage.tail = current  # Set the tail to the second to last item.
            self.storage.tail.next = current  # And the next as well.
            self.size -= 1  # Subtract one from the size.
            return value
        

# ### LAZY METHOD FOR MVP - FUNCTIONS. ####
# from singly_linked_list import LinkedList, Node
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


#### Answer to Number Three: ####
# When implementing a stack via Linked List vs an array, there is a significant increase in runtime complexity.
# Because arrays support random access by index, they are faster, with a runtime complexity of O(1) to access
# an element. Because Linked Lists work off sequential access, we need to traverse the list until the desired
# element has been reached. Because of this, runtime complexity is O(n), where n is the `nth` element of the list.
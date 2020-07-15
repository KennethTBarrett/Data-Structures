"""
### Doubly Linked Lists
 * The `ListNode` class, which represents a single node in the doubly-linked list, has already been implemented for you. Inspect this code and try to understand what it is doing to the best of your ability.
 * The `DoublyLinkedList` class itself should have the methods: `add_to_head`, `add_to_tail`, `remove_from_head`, `remove_from_tail`, `move_to_front`, `move_to_end`, `delete`, and `get_max`.
   * `add_to_head` replaces the head of the list with a new value that is passed in.
   * `add_to_tail` replaces the tail of the list with a new value that is passed in.
   * `remove_from_head` removes the head node and returns the value stored in it.
   * `remove_from_tail` removes the tail node and returns the value stored in it.
   * `move_to_front` takes a reference to a node in the list and moves it to the front of the list, shifting all other list nodes down. 
   * `move_to_end` takes a reference to a node in the list and moves it to the end of the list, shifting all other list nodes up. 
   * `delete` takes a reference to a node in the list and removes it from the list. The deleted node's `previous` and `next` pointers should point to each afterwards.
   * `get_max` returns the maximum value in the list. 
 * The `head` property is a reference to the first node and the `tail` property is a reference to the last node.
"""

"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
  

            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)  # New node to add to head.

        if not self.head and not self.tail:  # If head / tail don't exist...
            # Set both to our new node.
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head  # Set head's next to the new node.
            self.head.prev = new_node  # Set head's previous to the new node.
            self.head = new_node  # Set head as new node.
        self.length += 1  # Add one to the length.
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head:  # If our head exists...
            current = self.head  # The current value should be our head.
            if self.head is self.tail:  # If the head is the tail...
                self.tail = None  # Set the tail value to None.
            self.head = current.next  # Set the head to the `next` value of current.
            self.length -= 1  # Subtract one from our length.
            return current.value


    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)  # Our new node to add to the tail.
        if self.head: # If head exists...
            current = self.tail  # The current value should be our tail.
            while current.next:  # While there's still a next value...
                current = current.next  # Set current to it!
            new_node.prev = current  # Set the previous pointer to `current`
            current.next = new_node  # The next value of current should be set to our new node.
            self.tail = new_node  # Set the tail to be our new node.
            self.length += 1  # Add one to the length.
        else:  # Otherwise, if head doesn't exist...
            self.length += 1  # Add one to the length.
            # Set head / tail to be our new node.
            self.head = new_node
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        curr_tail = self.tail  # Storing the current tail in our memory to return.
        if curr_tail.prev:  # If there is a previous value...
            self.tail = curr_tail.prev  # Set the tail to that value.
        else:  # Otherwise...
            # Head and tail should both be None.
            self.tail = None
            self.head = None
        self.length -= 1  # Subtract one from our length.
        return curr_tail.value  # Return the original tail.
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        current = self.head  # Set current to the head to traverse Linked List.
        while current != node:  # While `current` isn't our node...
            current = current.next  # Go to the next value.
        current.next = self.head  # Set the current's next value to the head.
        current.prev = None  # Set the previous value to None...
        self.head = current  # And set the head to our current.
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        current = self.head  # Set current to traverse list.
        while current != node:  # While the current value isn't the node...
            current = current.next  # Set the next.
        if current.prev:  # If there's a previous value...
            before = current.prev  # Store the previous value of current
            before.next = current.next  # Set before's `next` value to current's `next` value.
            if node == self.tail:  # If the node is the tail...
                self.tail = before  # Set the tail to `before`
        if current.next:  # If current's next value exists...
            after = current.next  # Store the next value of current.
            after.prev = current.prev  # Set after's `prev` value to current's `prev` value.
            if node is self.head:  # If the node isn't the head...
                self.head = after  # Set the head to `after`
        
        prev_tail = self.tail  # This is our previous tail.
        prev_tail.next = current  # Set the `next` of it to be current.
        current.prev = prev_tail  # Set the previous value of current to be the previous tail.
        current.next = None  # Set the next value to be None.
        self.tail = current # Set the tail to be `current`

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        current = self.head  # For traversing list.
        while current != node:  # While current isn't the node...
            current = current.next  # Go to next.
        if node == self.head and node == self.tail:  # If head & tail are our node (only one node in the list)
            # Delete them.
            self.head = None
            self.tail = None
        if current.prev:  # If a previous value exists.
            before = current.prev  # Store the previous value of current.
            before.next = current.next  # Define the next value to be the next value of current.
            if node == self.tail:  # If the node is our tail...
                self.tail = before  # Set the tail to before.
        if current.next:  # If a next value exists within current...
            after = current.next  # Store the next value.
            after.prev = current.prev  # Set the previous value of that to be our current's previous value.
            if node == self.head:  # If the node is the head...
                self.head = after  # Set the head to `after`
        self.length -= 1  # Subtract one from the length.

    


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        current = self.head  # Set the current to traverse the list.
        max_value = current.value  # Set max value to be the value in our head.
        while current:  # While the value exists...
            if current.value > max_value:  # If it's greater than the max value...
                max_value = current.value  # Change the max value.
            current = current.next  # Go to the next value.
        return max_value


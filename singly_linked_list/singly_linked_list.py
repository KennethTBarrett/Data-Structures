class Node:
    """This is the node class for our LinkedList."""
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    """This is the class for our LinkedList."""
    def __init__(self):
        self.head = None
        self.tail = None 

    def add_to_head(self, value):
        # Create Node from the specified value.
        new_node = Node(value)
        # Check if both head and tail are empty. If so...
        if self.head is None and self.tail is None:
                # Have both head and tail referring to the single node... 
                self.head = new_node
                # and set the new node to be the tail.
                self.tail = new_node
        else:
            # These steps assume that the head is already referring
            # to a Node 
            # Set the old head's .next to refer to our new Node 
            self.head.set_next(new_node)
            # 3. Reassign self.head to refer to our new Node
            self.head = new_node

    def add_to_tail(self, value):
        # Create the Node from the value. 
        new_node = Node(value)
        # Check if both head and tail are empty. If so...
        if self.head is None and self.tail is None:
            # Have both head and tail referring to the single node... 
            self.head = new_node
            # and set the new node to be the tail.
            self.tail = new_node
        else:
            # These steps assume that the tail is already referring
            # to a Node 
            # Wet the old tail's .next to refer to the new Node 
            self.tail.set_next(new_node)
            # Reassign self.tail to refer to the new Node 
            self.tail = new_node

    def remove_head(self):
        # If our linked list is empty (no head, no tail)...
        if self.head is None and self.tail is None:
            return
        # Determine if there is more than one element in the linked list.
        if not self.head.get_next():  # If there is not...
            head = self.head 
            # Delete both the head and tail elements.
            self.head = None 
            self.tail = None 
            return head.get_value()

        val = self.head.get_value()
        # Set self.head to the Node after the head 
        self.head = self.head.get_next()

        return val

    def remove_tail(self):
        if self.head is None:
            return None
        
        current = self.head

        while current.get_next() and current.get_next() is not self.tail:
            current = current.get_next()
        value = self.tail.get_value()
        self.tail = current
        self.tail.set_next(None)
        return value

    def contains(self, value):
        if not self.head:
            return False
    
        # get a reference to the node we're currently at; update this as we 
        # traverse the list
        current = self.head
        # check to see if we're at a valid node 
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def get_max(self):
        if not self.head:
            return None
        # This is the largest value we've seen thus far.
        max_value = self.head.get_value()
        # reference to our current node as we traverse the list
        current = self.head.get_next()
        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.get_value() > max_value:
                # if so, update our max_value variable
                max_value = current.get_value()
            # update the current node to the next node in the list
            current = current.get_next()

        return max_value



if __name__ == "__main__":
    ll = LinkedList()
    # ll.add_to_tail(10)
    # ll.add_to_tail(3)
    # ll.remove_tail()
    # print(ll)

    breakpoint()
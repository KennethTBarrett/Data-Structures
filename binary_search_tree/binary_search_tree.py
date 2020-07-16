from stack import Stack
from queue import Queue

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # If the value is greater than or equal to the current value...
        if value >= self.value:
            # Check if there's a value to the right.
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        # If the value is less than the current value...
        elif value < self.value:
            # Check if there's a value to the left.
            if self.left is None:  # If there's not...
                self.left = BSTNode(value)  # Set it to the BSTNode.
            else:  # Otherwise...
                self.left.insert(value)  # Use recursion.

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:  # Check whether current value is our target.
            return True  # If so, return True.
        elif target < self.value:  # If the target is less than the value...
            if self.left == None:  # Check if there's a left. If not...
                return False  # Return false.
            else:  # Otherwise...
                return self.left.contains(target)  # Use recursion.
        elif target > self.value:  # If the target is greater than the value...
            if self.right is None:  # And there's nothing to our right...
                return False  # Return False
            else:  # If there is...
                return self.right.contains(target)  # Recursion.

    # Return the maximum value found in the tree
    def get_max(self):
        # Confirm that a higher value even exists...
        if self.right == None:  # If not...
            return self.value  # Return the value.
        return self.right.get_max()  # Return the maximum value.

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)  # Run function on root node.
        # Confirm there's a node to the left.
        if self.left == None:  # If not...
            pass  # Pass.
        else:  # If there is...
            self.left.for_each(fn)  # Recursion.
        # Confirm there's a node to the right.
        if self.right == None:  # If there's not...
            pass  # Pass.
        else:  # If there is...
            self.right.for_each(fn)  # Recusion.

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:  # If there's a left node (low to high)
            node.left.in_order_print(node.left)  # Recursion.
        print(node.value)  # Print the value.
        if node.right:  # If there's a right node...
            node.right.in_order_print(node.right)  # Recursion.

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # Because we're using BFT, I'm going to need to use the Queue data structure.
        queue_node = Queue()
        # Add the node to our queue.
        queue_node.enqueue(node)

        # While the queue isn't empty...
        while queue_node.size > 0:
            # Dequeue our node.
            dequeued = queue_node.dequeue()
            # Print the value of it.
            print(dequeued.value)

            # Now, we need to add the nodes to the next level.
            if dequeued.left:  # If there is a node to the left...
                # Add it to our queue.
                queue_node.enqueue(dequeued.left)
            if dequeued.right:  # If there is a node to the right...
                # Add it to our queue.
                queue_node.enqueue(dequeued.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # Because we're using DFT, I'm going to need to use the Stack data structure.
        stack_node = Stack()
        # Add the node into our stack.
        stack_node.push(node)

        # While the stack isn't empty...
        while stack_node.size > 0:
            # Delete the node from the Stack.
            deleted = stack_node.pop()
            # Print value of that node.
            print(deleted.value)

            # Now, we need to add the nodes to the next level.
            if deleted.left:
                stack_node.push(deleted.left)
            if deleted.right:
                stack_node.push(deleted.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

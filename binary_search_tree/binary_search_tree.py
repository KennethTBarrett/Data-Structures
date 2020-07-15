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
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

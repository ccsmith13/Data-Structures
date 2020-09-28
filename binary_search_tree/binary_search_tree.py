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
        if value < self.value: 
            if self.left is None: 
                self.left = BSTNode(value)
            else:
                return self.left.insert(value)
        else:
            if self.right is None: 
                self.right = BSTNode(value)
            else: 
                return self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if self.value is target 
        if self.value == target: 
            return True
        else: 
            if target < self.value: 
                if self.left is not None:
                    return self.left.contains(target)
                else: 
                    return False
            elif target > self.value: 
                if self.right is not None: 
                    return self.right.contains(target) 
                else: 
                    return False

    # Return the maximum value found in the tree
    def get_max(self):
        # go right until you cannot anymore 
        # return value at far right
        if self.right is None: 
            return self.value
        else: 
            while self.right is not None: 
                if self.value < self.right.value: 
                    return self.right.get_max()
                else: 
                    return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # one side then the other 
        # fn(value)
        fn(self.value)
        # base case: no children 
        if self.left is None and self.right is None: 
            return
         # recursive case: 1 or more children 
         # go left, call fn for each node
        if self.left:
            self.left.for_each(fn)
        # go right, call fn for each node
        if self.right: 
            self.right.for_each(fn)

    def iterative_depth_first_for_each(self, fn):
        # DFT: LIFO
        # we'll use a stack 
        stack = []
        stack.append(self)
        
        while len(stack) > 0:
            #pop the current node from the stack
            current = stack.pop()

            #add the current node's right child first 
            if current.right:
                stack.append(current.right)

            #add the current node's left child 
            if current.left:
                stack.append(current.left)

            #call the anonymous function 
            fn(current.value)
    
    def iterative_breadth_first_for_each(self, fn):
        # BFT: FIFO
        # we'll use a queue 
        from collections import deque
        queue = deque()
        queue.append(self)

        while len(queue) > 0:
            current = queue.popleft()

            if current.left: 
                queue.append(current.left)

            if current.right: 
                queue.append(current.right)
            
            fn(current.value)
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.value:
            if self.left: 
                self.left.in_order_print()

            print(self.value)

            if self.right:
                self.right.in_order_print()

            

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        from collections import deque
        queue = deque()
        queue.append(self)

        while len(queue) > 0:
            current = queue.popleft()

            if current.left: 
                queue.append(current.left)

            if current.right: 
                queue.append(current.right)
            
            print(current.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        stack = []
        stack.append(self)
        
        if self is None: 
            return 

        while len(stack) > 0:
            current = stack.pop()

            if current.right:
                stack.append(current.right)

            if current.left:
                stack.append(current.left)

            print(current.value)

    # Stretch Goals -------------------------
    # Note: Research may be required
    def in_order_dft(self):
        
        if self.left: 
            self.left.in_order_dft()
        
        print(self.value)

        if self.right: 
            self.right.in_order_dft()

    # Print Pre-order recursive DFT
    def pre_order_dft(self):

        print(self.value)
        
        if self.left: 
            self.left.pre_order_dft()

        if self.right: 
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        
        if self.left: 
            self.left.pre_order_dft()

        if self.right: 
            self.right.pre_order_dft()
        
        print(self.value)

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()  

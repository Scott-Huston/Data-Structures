import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # checks whether value should go to left or right
        # if left/right is None, then add a new tree with the value there
        # otherwise, recursively call insert on that subtree
        if self.value > value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        
        else:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):

        # base case for recursion
        if self.value == target:
            return True
        
        if self.value > target:
            if self.left == None:
                return False
            else:
                return self.left.contains(target)
        
        else:
            if self.right == None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        current_tree = self
        while current_tree.right != None:
            current_tree = current_tree.right
        
        return current_tree.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # call the function on value of current tree
        cb(self.value)

        # recursively call for_each on both branches if they exist
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):

        if node.left:
            node.in_order_print(node.left)
        
        print(node.value)
        
        if node.right:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()

        q.enqueue(node)
        # main loop
        while q.len() > 0:
            current_node = q.dequeue()

            print(current_node.value)

            if current_node.left:
                q.enqueue(current_node.left)
            
            if current_node.right:
                q.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        s = Stack()

        s.push(node)
        while s.len() > 0:
            current_node = s.pop()

            print(current_node.value)

            if current_node.right:
                s.push(current_node.right)
            
            if current_node.left:
                s.push(current_node.left)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

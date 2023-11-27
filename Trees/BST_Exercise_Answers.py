# BST: Constructor

# Define the Node class to create nodes for the tree
class Node:
    # Constructor initializes a node with a value
    def __init__(self, value):
        # Store the node's value
        self.value = value
        # Initialize left child to None (no left child)
        self.left = None
        # Initialize right child to None (no right child)
        self.right = None
 
 
# Define the BinarySearchTree class to create the tree
class BinarySearchTree:
    # Constructor initializes an empty tree
    def __init__(self):
        # Set the root of the tree to None (empty tree)
        self.root = None

# BST: Insert

def insert(self, value):
    # Create a new node with the provided value
    new_node = Node(value)
 
    # Check if the tree is empty
    if self.root is None:
        # Make the new node the root and return True
        self.root = new_node
        return True
 
    # Start at the root of the tree
    temp = self.root
 
    # Loop until the correct spot is found
    while (True):
 
        # Check for duplicate values
        if new_node.value == temp.value:
            # Duplicate found, return False
            return False
 
        # Check if the new value is less than current node's value
        if new_node.value < temp.value:
            # Is the left child spot empty?
            if temp.left is None:
                # Insert new node as left child, return True
                temp.left = new_node
                return True
            # If not empty, move to left child
            temp = temp.left
 
        # If new value is greater, go to the right child
        else:
            # Is the right child spot empty?
            if temp.right is None:
                # Insert new node as right child, return True
                temp.right = new_node
                return True
            # If not empty, move to right child
            temp = temp.right

# BST: Contains

def contains(self, value):
    # Start by setting 'temp' to the root of the tree
    temp = self.root
    
    # Loop until 'temp' becomes None (end of tree)
    while (temp is not None):
        
        # If value to find is less than the current node's value
        if value < temp.value:
            # Move 'temp' to the left child and continue loop
            temp = temp.left
            
        # If value to find is greater than the current node's value
        elif value > temp.value:
            # Move 'temp' to the right child and continue loop
            temp = temp.right
            
        # If value is neither less nor greater, it must be equal
        else:
            # Value found! Return True.
            return True
            
    # If loop ends, value was not found in tree. Return False.
    return False
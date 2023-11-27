# rBST: Contains

def __r_contains(self, current_node, value):
    if current_node == None: 
        return False      
    if value == current_node.value:
        return True 
    if value < current_node.value:
        return self.__r_contains(current_node.left, value) 
    if value > current_node.value:
        return self.__r_contains(current_node.right, value)
 
def r_contains(self, value):
    return self.__r_contains(self.root, value)

def __r_contains(self, current_node, value):
    # If current_node is None, we have reached a leaf node and
    # the value is not present in the tree.
    if current_node == None: 
        return False      
    # If the value matches the value of the current_node, we have found
    # the value and return True.
    if value == current_node.value:
        return True 
    # If the value is less than the value of the current_node, we recurse
    # on the left subtree.
    if value < current_node.value:
        return self.__r_contains(current_node.left, value) 
    # If the value is greater than the value of the current_node, we recurse
    # on the right subtree.
    if value > current_node.value:
        return self.__r_contains(current_node.right, value)
 
def r_contains(self, value):
    # The r_contains method calls the private helper method __r_contains
    # with the root node of the tree and the value to search for.
    # It returns the output of __r_contains.
    return self.__r_contains(self.root, value)

# rBST: Insert

def __r_insert(self, current_node, value):
    if current_node == None: 
        return Node(value)   
    if value < current_node.value:
        current_node.left = self.__r_insert(current_node.left, value)
    if value > current_node.value:
        current_node.right = self.__r_insert(current_node.right, value) 
    return current_node    
 
def r_insert(self, value):
    if self.root == None: 
        self.root = Node(value)
    self.__r_insert(self.root, value)

def __r_insert(self, current_node, value):
    # If current_node is None, we have reached a leaf node and 
    # insert a new node with the given value.
    if current_node == None: 
        return Node(value)   
    # If the value is less than the value of the current_node, we insert
    # the value into the left subtree.
    if value < current_node.value:
        current_node.left = self.__r_insert(current_node.left, value)
    # If the value is greater than the value of the current_node, we insert
    # the value into the right subtree.
    if value > current_node.value:
        current_node.right = self.__r_insert(current_node.right, value) 
    # Return the modified current_node after inserting the value.
    return current_node    
 
def r_insert(self, value):
    # If the tree is empty, create a new node and make it the root node.
    if self.root == None: 
        self.root = Node(value)
    # Call the private helper method __r_insert with the root node and the value
    # to be inserted. 
    self.__r_insert(self.root, value)

# rBST: Minimum Value

def min_value(self, current_node):
    while current_node.left is not None:
        current_node = current_node.left
    return current_node.value

def min_value(self, current_node):
    # Iterate until no left child is found
    while current_node.left is not None:
        # Move to the left child of current node
        current_node = current_node.left
    # Return the value of the leftmost node
    return current_node.value

# rBST: Delete

def __delete_node(self, current_node, value):
    if current_node == None:
        return None
    if value < current_node.value:
        current_node.left = self.__delete_node(current_node.left, value)
    elif value > current_node.value:
        current_node.right = self.__delete_node(current_node.right, value)
    else:
        if current_node.left == None and current_node.right == None:
            return None
        elif current_node.left == None:
            current_node = current_node.right
        elif current_node.right == None:
            current_node = current_node.left
        else:
            sub_tree_min = self.min_value(current_node.right)
            current_node.value = sub_tree_min
            current_node.right = self.__delete_node(current_node.right, sub_tree_min)
    return current_node
 
def delete_node(self, value):
    self.root = self.__delete_node(self.root, value)

def __delete_node(self, current_node, value):
    # Return None if the current node is None
    if current_node == None:
        return None
    # Traverse the left subtree if value is smaller
    if value < current_node.value:
        current_node.left = self.__delete_node(current_node.left, value)
    # Traverse the right subtree if value is larger
    elif value > current_node.value:
        current_node.right = self.__delete_node(current_node.right, value)
    # If value is found, delete the node
    else:
        # Case 1: No children, return None to delete
        if current_node.left == None and current_node.right == None:
            return None
        # Case 2: No left child, return right child
        elif current_node.left == None:
            current_node = current_node.right
        # Case 3: No right child, return left child
        elif current_node.right == None:
            current_node = current_node.left
        # Case 4: Two children, find min in right subtree
        else:
            sub_tree_min = self.min_value(current_node.right)
            current_node.value = sub_tree_min
            current_node.right = self.__delete_node(current_node.right, sub_tree_min)
    # Return the current node after deletion
    return current_node
 
def delete_node(self, value):
    # Call the helper method to delete the node
    # You may see other implementations that write it this way:
    # self.__delete_node(self.root, value)
    # but that way will not work when removing the root node
    self.root = self.__delete_node(self.root, value)
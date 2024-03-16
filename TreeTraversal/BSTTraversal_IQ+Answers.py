# BST: Validate BST

def is_valid_bst(self):
    node_values = self.dfs_in_order()
    for i in range(1, len(node_values)):
        if node_values[i] <= node_values[i-1]:
            return False
    return True

def is_valid_bst(self):

# Get node values of the binary search tree in ascending order
    
    node_values = self.dfs_in_order()
    
# Iterate through the node values using a for loop
    
    for i in range(1, len(node_values)):
        
# Check if each node value is greater than the previous node value
        
        if node_values[i] <= node_values[i-1]:
            
# If node values are not sorted in ascending order, the binary
# search tree is not valid, so return False

            return False

# If all node values are sorted in ascending order, the binary search tree
# is a valid binary search tree, so return True
    
    return True

# BST: Kth Smallest Node

def kth_smallest(self, k):
    stack = []
    node = self.root
        
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
            
        node = stack.pop()
        k -= 1
        if k == 0:
            return node.value
        
        node = node.right
            
    return None

def kth_smallest(self, k):
        
# create a stack to hold nodes

        stack = []    
        
# start at the root of the tree      

        temp = self.root    
        
        while stack or temp:
            
# traverse to the leftmost node
            
            while temp: 
                
# add the node to the stack                
                
                stack.append(temp)      
                temp = temp.left
            
# pop the last node added to the stack
            
            temp = stack.pop()           
            k -= 1
            
# if kth smallest element is found, return the value
            
            if k == 0:                  
                return temp.value
            
# move to the right child of the node
            
            temp = temp.right           
            
# if k is greater than the number of nodes in the tree, return None

        return None

# BST: Kth Smallest Node (Recursive Solution)

def kth_smallest(self, k):
    self.kth_smallest_count = 0
    return self.kth_smallest_helper(self.root, k)
 
def kth_smallest_helper(self, node, k):
    if node is None:
        return None
 
    left_result = self.kth_smallest_helper(node.left, k)
    if left_result is not None:
        return left_result
 
    self.kth_smallest_count += 1
    if self.kth_smallest_count == k:
        return node.value
 
    right_result = self.kth_smallest_helper(node.right, k)
    if right_result is not None:
        return right_result
 
    return None

def kth_smallest(self, k):

# initialize the number of nodes visited to 0
        
        self.kth_smallest_count = 0

# call the helper function with the root node and k
        
        return self.kth_smallest_helper(self.root, k)
 
def kth_smallest_helper(self, node, k):
    if node is None:
        
# if the current node is None, return None

        return None
 
# recursively call the helper function on the left child of the node and store the result in left_result
    
    left_result = self.kth_smallest_helper(node.left, k)
    if left_result is not None:
        
# if left_result is not None, return it
        
        return left_result
 
# increment the number of nodes visited by 1
    
    self.kth_smallest_count += 1
    if self.kth_smallest_count == k:
        
# if the kth smallest element is found, return the value of the current node
        return node.value
 
# recursively call the helper function on the right child of the node and store the result in right_result
    
    right_result = self.kth_smallest_helper(node.right, k)
    if right_result is not None:

# if right_result is not None, return it
        
        return right_result
 
# if the kth smallest element is not found, return None
    
    return None
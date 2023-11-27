# BFS

def BFS(self):
    current_node = self.root
    queue = []
    results = []
    queue.append(current_node)
 
    while len(queue) > 0:
        current_node = queue.pop(0)
        results.append(current_node.value)
        if current_node.left is not None:
            queue.append(current_node.left)
        if current_node.right is not None:
            queue.append(current_node.right)
    return results

def BFS(self):
    # set current_node to the root of the tree
    current_node = self.root
    
    # create an empty queue to store nodes to visit
    queue = []
    
    # create an empty list to store the values of visited nodes
    results = []
    
    # add the root node to the queue
    queue.append(current_node)
 
    # continue until all nodes have been visited
    while len(queue) > 0:
        # remove the first node from the queue
        current_node = queue.pop(0)
        
        # add the value of the visited node to the results list
        results.append(current_node.value)
        
        # if the visited node has a left child, add it to the queue
        if current_node.left is not None:
            queue.append(current_node.left)
        
        # if the visited node has a right child, add it to the queue
        if current_node.right is not None:
            queue.append(current_node.right)
 
    # return the list of visited node values
    return results

# DFS: PreOrder

def dfs_pre_order(self):
    results = []
    def traverse(current_node):
        results.append(current_node.value)
        if current_node.left is not None:
            traverse(current_node.left)
        if current_node.right is not None:
            traverse(current_node.right)
    traverse(self.root)
    return results

def dfs_pre_order(self):
    results = []  # create an empty list to store the values of visited nodes
 
    def traverse(current_node):
        # append the value of the current node to the results list
        results.append(current_node.value)
 
        # if the current node has a left child, recursively traverse it
        if current_node.left is not None:
            traverse(current_node.left)
 
        # if the current node has a right child, recursively traverse it
        if current_node.right is not None:
            traverse(current_node.right)
 
    # start the pre-order traversal from the root of the tree
    traverse(self.root)
 
    # return the list of visited node values
    return results

# DFS: PostOrder

def dfs_post_order(self):
    results = []
    def traverse(current_node):
        if current_node.left is not None:
            traverse(current_node.left)
        if current_node.right is not None:
            traverse(current_node.right)
        results.append(current_node.value)
    traverse(self.root)
    return results


def dfs_post_order(self):
    results = []  # create an empty list to store the values of visited nodes
 
    def traverse(current_node):
        # if the current node has a left child, recursively traverse it
        if current_node.left is not None:
            traverse(current_node.left)
 
        # if the current node has a right child, recursively traverse it
        if current_node.right is not None:
            traverse(current_node.right)
 
        # append the value of the current node to the results list
        results.append(current_node.value)
 
    # start the post-order traversal from the root of the tree
    traverse(self.root)
 
    # return the list of visited node values
    return results

# DFS: InOrder

def dfs_in_order(self):
    results = []
    def traverse(current_node):
        if current_node.left is not None:
            traverse(current_node.left)
        results.append(current_node.value) 
        if current_node.right is not None:
            traverse(current_node.right)          
    traverse(self.root)
    return results

def dfs_in_order(self):
    results = []  # create an empty list to store the values of visited nodes
 
    def traverse(current_node):
        # if the current node has a left child, recursively traverse it
        if current_node.left is not None:
            traverse(current_node.left)
 
        # append the value of the current node to the results list
        results.append(current_node.value)
 
        # if the current node has a right child, recursively traverse it
        if current_node.right is not None:
            traverse(current_node.right)
 
    # start the in-order traversal from the root of the tree
    traverse(self.root)
 
    # return the list of visited node values
    return results
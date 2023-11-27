# LL: Find Middle Node IQ with Answer

def find_middle_node(self):
    slow = self.head
    fast = self.head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

def find_middle_node(self):
    # 1. Initialize two pointers: 'slow' and 'fast', 
    # both starting from the head.
    slow = self.head
    fast = self.head
 
    # 2. Iterate as long as 'fast' pointer and its next 
    # node are not None.
    # This ensures we don't get an error trying to access
    # a non-existent node.
    while fast is not None and fast.next is not None:
        
        # 2.1. Move 'slow' one step ahead.
        # This covers half the distance that 'fast' covers.
        slow = slow.next
        
        # 2.2. Move 'fast' two steps ahead.
        # Thus, when 'fast' reaches the end, 'slow' 
        # will be at the middle.
        fast = fast.next.next
 
    # 3. By now, 'fast' has reached or surpassed the end, 
    # and 'slow' is positioned at the middle node.
    # Return the 'slow' pointer, which points to 
    # the middle node.
    return slow

# LL: Write a method called "has_loop" IQ with Answer

def has_loop(self):
    slow = self.head
    fast = self.head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
    
def has_loop(self):
# 1. Initialize two pointers: 'slow' and 'fast', 
# both starting from the head.
    slow = self.head
    fast = self.head
 
# 2. Continue traversal as long as the 'fast' pointer 
# and its next node aren't None.
# This ensures we don't run into errors trying to 
# access non-existent nodes.
    while fast is not None and fast.next is not None:

    # 2.1. Move 'slow' pointer one step ahead.
        slow = slow.next
        
    # 2.2. Move 'fast' pointer two steps ahead.
        fast = fast.next.next
        
    # 2.3. Check for cycle: If 'slow' and 'fast' meet,
    # it means there's a cycle in the linked list.
        if slow == fast:
        # 2.3.1. If they meet, return True 
        # indicating the list has a loop.
            return True
 
# 3. If we've gone through the entire list and 
# the pointers never met, then the list doesn't have a loop.
    return False

# LL: Find Kth Node From End IQ with Answer

def find_kth_from_end(ll, k):
    slow = fast = ll.head   
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
 
    while fast:
        slow = slow.next
        fast = fast.next
        
    return slow

def find_kth_from_end(ll, k):
    # 1. Initialize two pointers, 'slow' and 'fast', both pointing to the 
    # starting node of the linked list.
    slow = fast = ll.head   
    
    # 2. Move the 'fast' pointer 'k' positions ahead.
    for _ in range(k):
        # 2.1. If at any point during these 'k' movements, the 'fast' 
        # pointer reaches the end of the list, then it means the list 
        # has less than 'k' nodes, and thus, returning None is appropriate.
        if fast is None:
            return None
        
        # 2.2. Move the 'fast' pointer to the next node.
        fast = fast.next
 
    # 3. Now, move both 'slow' and 'fast' pointers one node at a time until 
    # the 'fast' pointer reaches the end of the list. Since the 'fast' pointer 
    # is already 'k' nodes ahead of the 'slow' pointer, by the time 'fast' 
    # reaches the end, 'slow' will be at the kth node from the end.
    while fast:
        slow = slow.next
        fast = fast.next
        
    # 4. Return the 'slow' pointer, which is now pointing to the kth node 
    # from the end.
    return slow

# LL: Partition List

def partition_list(self, x):
    if not self.head:
        return None
    
    dummy1 = Node(0)
    dummy2 = Node(0)
    prev1 = dummy1
    prev2 = dummy2
    current = self.head
    
    while current:
        if current.value < x:
            prev1.next = current
            prev1 = current
        else:
            prev2.next = current
            prev2 = current
        current = current.next
    
    prev1.next = None
    prev2.next = None
    prev1.next = dummy2.next
    
    self.head = dummy1.next

def partition_list(self, x):
    # 1. Edge case: Check if the list is empty. If so, exit.
    if not self.head:
        return None
 
    # 2. Create two dummy nodes: 
    # dummy1 for nodes with values less than x 
    # and dummy2 for nodes with values greater or equal to x.
    dummy1 = Node(0)
    dummy2 = Node(0)
 
    # 3. Initialize two pointers (prev1 and prev2) at the dummy nodes.
    # They will be used to build the two separate lists.
    prev1 = dummy1
    prev2 = dummy2
 
    # 4. Start iterating from the head of the original list.
    current = self.head
 
    # 5. Traverse the entire list.
    while current:
        # 5.1. If the current node's value is less than x:
        if current.value < x:
            # 5.1.1. Attach it to the end of the list starting at dummy1.
            prev1.next = current
            # 5.1.2. Move the prev1 pointer forward.
            prev1 = current
        # 5.2. Otherwise:
        else:
            # 5.2.1. Attach it to the end of the list starting at dummy2.
            prev2.next = current
            # 5.2.2. Move the prev2 pointer forward.
            prev2 = current
        
        # 5.3. Move to the next node in the original list.
        current = current.next
 
    # 6. End the two lists. Set the next pointers of prev1 and prev2 to None.
    prev1.next = None
    prev2.next = None
 
    # 7. Link the end of the first list (the one that started at dummy1) 
    # to the beginning of the second list (the one that started at dummy2).
    prev1.next = dummy2.next
 
    # 8. Update the head of the linked list to point to the beginning 
    # of the partitioned list.
    self.head = dummy1.next

# LL: Remove Duplicates

def remove_duplicates(self):
    values = set()
    previous = None
    current = self.head
    while current:
        if current.value in values:
            previous.next = current.next
            self.length -= 1
        else:
            values.add(current.value)
            previous = current
        current = current.next

def remove_duplicates(self):
    # 1. Initialize a set called 'values' to store unique node values.
    values = set()
    
    # 2. Initialize 'previous' to None. 
    # This will point to the last node we've seen that had a unique value.
    previous = None
    
    # 3. Start at the head of the linked list.
    current = self.head
 
    # 4. Traverse through the linked list.
    while current:
        # 4.1. Check if the value of the current node is already in the set.
        if current.value in values:
            # 4.1.1. If yes, bypass this node by pointing the next of 
            # 'previous' to the next of 'current'.
            previous.next = current.next
            
            # 4.1.2. Decrement the length of the list.
            self.length -= 1
        else:
            # 4.2. If not, add the value to the set.
            values.add(current.value)
            
            # 4.2.1. Update the 'previous' to point to 'current' now.
            previous = current
 
        # 4.3. Move to the next node in the list.
        current = current.next

# LL: Binary to Decimal

def binary_to_decimal(self):
    num = 0
    current = self.head
    while current:
        num = num * 2 + current.value
        current = current.next
    return num

def binary_to_decimal(self):
    # 1. Initialize a variable 'num' to 0. This will be used to accumulate the 
    # decimal value as we traverse the linked list.
    num = 0
    
    # 2. Start at the head of the linked list.
    current = self.head
 
    # 3. Traverse through the linked list.
    while current:
        # 3.1. For each node, left shift the accumulated value by 1 position. 
        # This is the same as multiplying by 2. This step ensures that we are 
        # moving to the next binary position.
        # 
        # Example: If num is '10' (binary for 2) and next node value is '1', 
        # left shifting '10' results in '100' (binary for 4). 
        # Now, adding the next node value gives '101' (binary for 5).
        num = num * 2
        
        # 3.2. Add the current node's value (which should be either 0 or 1) 
        # to the accumulated value 'num'.
        num = num + current.value
        
        # OR both the above steps can be combined as:
        # num = num * 2 + current.value
        
        # 3.3. Move to the next node in the list.
        current = current.next
 
    # 4. Return the accumulated decimal value.
    return num

# LL: Reverse Between

def reverse_between(self, start_index, end_index):
    if self.length <= 1:
        return
    
    dummy_node = Node(0)
    dummy_node.next = self.head
    previous_node = dummy_node
    
    for i in range(start_index):
        previous_node = previous_node.next
    
    current_node = previous_node.next
    
    for i in range(end_index - start_index):
        node_to_move = current_node.next
        current_node.next = node_to_move.next
        node_to_move.next = previous_node.next
        previous_node.next = node_to_move
    
    self.head = dummy_node.next

def reverse_between(self, start_index, end_index):
    # 1. Edge Case: If list has only one node or none, exit.
    if self.length <= 1:
        return
 
    # 2. Create a dummy node to simplify head operations.
    dummy_node = Node(0)
    dummy_node.next = self.head
 
    # 3. Init 'previous_node', pointing just before reverse starts.
    previous_node = dummy_node
 
    # 4. Move 'previous_node' to its position.
    # It'll be at index 'start_index - 1' after this loop.
    for i in range(start_index):
        previous_node = previous_node.next
 
    # 5. Init 'current_node' at 'start_index', start of reversal.
    current_node = previous_node.next
 
    # 6. Begin reversal:
    # Loop reverses nodes between 'start_index' and 'end_index'.
    for i in range(end_index - start_index):
        # 6.1. 'node_to_move' is next node we want to reverse.
        node_to_move = current_node.next
 
        # 6.2. Disconnect 'node_to_move', point 'current_node' after it.
        current_node.next = node_to_move.next
 
        # 6.3. Insert 'node_to_move' at new position after 'previous_node'.
        node_to_move.next = previous_node.next
 
        # 6.4. Link 'previous_node' to 'node_to_move'.
        previous_node.next = node_to_move
 
    # 7. Update list head if 'start_index' was 0.
    self.head = dummy_node.next

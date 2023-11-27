# DLL: Swap First and Last IQ with Answer

def swap_first_last(self):
    if self.head is None or self.head == self.tail:
        return
    self.head.value, self.tail.value = self.tail.value, self.head.value

def swap_first_last(self):
    # 1. Check if the doubly linked list is empty or has only one node. 
    # If so, there's nothing to swap, hence exit the function early.
    if self.head is None or self.head == self.tail:
        return
    
    # 2. If the list has more than one node, swap the values of the 
    # head (first node) and tail (last node).
    # Note: We're only exchanging the data stored in the nodes, 
    # rather than altering the structure of the linked list itself.
    self.head.value, self.tail.value = self.tail.value, self.head.value

# DLL: Reverse IQ with Answer

def reverse(self):
    temp = self.head
    while temp is not None:
        temp.prev, temp.next = temp.next, temp.prev
        temp = temp.prev
    self.head, self.tail = self.tail, self.head

def reverse(self):
    temp = self.head
    while temp is not None:
        # swap the prev and next pointers of node points to
        temp.prev, temp.next = temp.next, temp.prev
            
        # move to the next node
        temp = temp.prev
            
    # swap the head and tail pointers
    self.head, self.tail = self.tail, self.head

# DLL: Palindrome Checker with Answer

def is_palindrome(self):
    if self.length <= 1:
        return True
    forward_node = self.head
    backward_node = self.tail
    for i in range(self.length // 2):
        if forward_node.value != backward_node.value:
            return False
        forward_node = forward_node.next
        backward_node = backward_node.prev
    return True

def is_palindrome(self):
    # 1. If the length of the doubly linked list is 0 or 1, then 
    # the list is trivially a palindrome. 
    if self.length <= 1:
        return True
    
    # 2. Initialize two pointers: 'forward_node' starting at the head 
    # and 'backward_node' starting at the tail.
    forward_node = self.head
    backward_node = self.tail
    
    # 3. Traverse through the first half of the list. We only need to 
    # check half because we're comparing two nodes at once: one from 
    # the beginning and one from the end.
    for i in range(self.length // 2):
        # 3.1. Compare the values of 'forward_node' and 'backward_node'. 
        # If they're different, the list is not a palindrome.
        if forward_node.value != backward_node.value:
            return False
        
        # 3.2. Move the 'forward_node' one step towards the tail and 
        # the 'backward_node' one step towards the head for the next iteration.
        forward_node = forward_node.next
        backward_node = backward_node.prev
 
    # 4. If we've gone through the first half of the list without 
    # finding any non-matching node values, then the list is a palindrome.
    return True

# DLL: Swap Nodes in Pairs

def swap_pairs(self):
    dummy_node = Node(0)
    dummy_node.next = self.head
    previous_node = dummy_node
    
    while self.head and self.head.next:
        first_node = self.head
        second_node = self.head.next
    
        previous_node.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node
    
        second_node.prev = previous_node
        first_node.prev = second_node
    
        if first_node.next:
            first_node.next.prev = first_node
    
        self.head = first_node.next
        previous_node = first_node
    
    self.head = dummy_node.next
    
    if self.head:
        self.head.prev = None

def swap_pairs(self):
    # Step 1: Initialize a dummy node to act as a placeholder
    # for the start of the list.
    dummy_node = Node(0)
 
    # Connect this dummy node to the actual head of the list.
    # This simplifies the swapping process.
    dummy_node.next = self.head
 
    # Step 2: Initialize 'previous_node' to 'dummy_node'.
    # This helps us remember the node just before the pair
    # we are about to swap.
    previous_node = dummy_node
 
    # Step 3: Loop through the list as long as there are pairs
    # of nodes available to swap.
    while self.head and self.head.next:
 
        # Identify the first node in the pair to be swapped.
        first_node = self.head
 
        # Identify the second node in the pair to be swapped.
        second_node = self.head.next
 
        # Update 'previous_node' to point to 'second_node',
        # effectively skipping over 'first_node'.
        previous_node.next = second_node
 
        # Connect 'first_node' to the node that comes after
        # 'second_node'. This ensures we don't lose the
        # rest of the list.
        first_node.next = second_node.next
 
        # Swap 'first_node' and 'second_node' by connecting
        # 'second_node' back to 'first_node'.
        second_node.next = first_node
 
        # Update the 'prev' pointers for both 'first_node'
        # and 'second_node' to maintain the doubly-linked
        # structure.
        second_node.prev = previous_node
        first_node.prev = second_node
 
        # If there's a node after 'first_node', update its
        # 'prev' to point back to 'first_node'.
        if first_node.next:
            first_node.next.prev = first_node
 
        # Move the 'head' to the node just after 'first_node'
        # to prepare for the next iteration.
        self.head = first_node.next
 
        # Update 'previous_node' to point to 'first_node'
        # for the next pair to swap.
        previous_node = first_node
 
    # After the loop, set the new head of the list to the
    # node that comes after 'dummy_node'.
    self.head = dummy_node.next
 
    # Make sure the new head's 'prev' is set to None, as it
    # is now the first node in the list.
    if self.head:
        self.head.prev = None

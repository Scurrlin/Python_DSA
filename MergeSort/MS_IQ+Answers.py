# MS: Merge Two Sorted LL

def merge(self, other_list):
    other_head = other_list.head
    dummy = Node(0)
    current = dummy
 
    while self.head is not None and other_head is not None:
        if self.head.value < other_head.value:
            current.next = self.head
            self.head = self.head.next
        else:
            current.next = other_head
            other_head = other_head.next
        current = current.next
 
    if self.head is not None:
        current.next = self.head
    else:
        current.next = other_head
        self.tail = other_list.tail

    self.head = dummy.next
    self.length += other_list.length

# Method to merge a linked list with another linked list
def merge(self, other_list):
    
# Get the head node of the other linked list
    other_head = other_list.head
    
# Create a dummy node to hold the merged list
    dummy = Node(0)
    
# Set the current node to the dummy node
    current = dummy
 
# Loop while both lists still have nodes
    while self.head is not None and other_head is not None:
        
# Compare the values of the first nodes in each list
        if self.head.value < other_head.value:
            
# If the value in the first list is smaller,
# add it to the current node and move to the next node in the first list
            current.next = self.head
            self.head = self.head.next
        else:
            
# Otherwise, add the value from the second list
# and move to the next node in the second list
            current.next = other_head
            other_head = other_head.next
            
# Move the current node to the next position
        current = current.next
 
# If the first list still has nodes left, add them to the current node
    if self.head is not None:
        current.next = self.head
    else:
        
# If the second list still has nodes left, add them to the current node
        current.next = other_head

# Update the tail of the merged list to be the tail of the second list
        self.tail = other_list.tail
 
# Set the head of the merged list to the next node after the dummy node
    self.head = dummy.next
    
# Update the length of the merged list
    self.length += other_list.length
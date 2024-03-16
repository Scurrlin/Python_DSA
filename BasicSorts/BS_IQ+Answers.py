# BS: Bubble Sort of LL

def bubble_sort(self):
    if self.length < 2:
        return
        
    sorted_until = None
        
    while sorted_until != self.head.next:
        current = self.head
        while current.next != sorted_until:
            next_node = current.next
            if current.value > next_node.value:
                current.value, next_node.value = next_node.value, current.value
            current = current.next
        sorted_until = current

def bubble_sort(self):

# Check if the list has less than 2 elements
    if self.length < 2:
        return
    
# Initialize the sorted_until pointer to None
    sorted_until = None
    
# Continue sorting until sorted_until reaches the second node
    while sorted_until != self.head.next:
        
# Initialize current pointer to head of the list
        current = self.head
        
# Iterate through unsorted portion of the list until sorted_until
        while current.next != sorted_until:
            next_node = current.next
            
# Swap current and next_node values if current is greater
            if current.value > next_node.value:
                current.value, next_node.value = next_node.value, current.value
            
# Move current pointer to next node
            current = current.next
        
# Update sorted_until pointer to the last node processed
        sorted_until = current

# BS: Selection Sort of LL

def selection_sort(self):
    if self.length < 2:
        return
    current = self.head
    while current.next is not None:
        smallest = current
        inner_current = current.next
        while inner_current is not None:
            if inner_current.value < smallest.value:
                smallest = inner_current
            inner_current = inner_current.next
        if smallest != current:
            current.value, smallest.value = smallest.value, current.value        
        current = current.next
    self.tail = current

# Define a method to sort a linked list in ascending order 
# using the selection sort algorithm
def selection_sort(self):
    
# If the linked list has less than 2 elements, it is already sorted
    if self.length < 2:
        return
 
# Start with the first node as the current node
    current = self.head
 
# While there is at least one more node after the current node
    while current.next is not None:

# Assume the current node has the smallest value so far
        smallest = current

# Start with the next node as the inner current node
        inner_current = current.next
        
# Find the node with the smallest value among the remaining nodes
        while inner_current is not None:
            if inner_current.value < smallest.value:
                smallest = inner_current
            inner_current = inner_current.next
        
# If the node with the smallest value is not the current node, swap their values
        if smallest != current:
            current.value, smallest.value = smallest.value, current.value        
 
# Move to the next node
        current = current.next
    
# Set the tail of the linked list to the last node processed
    self.tail = current

# BS: Insertion Sort of LL

def insertion_sort(self):
    if self.length < 2:
        return
        
    sorted_list_head = self.head
    unsorted_list_head = self.head.next
    sorted_list_head.next = None
        
    while unsorted_list_head is not None:
        current = unsorted_list_head
        unsorted_list_head = unsorted_list_head.next
            
        if current.value < sorted_list_head.value:
            current.next = sorted_list_head
            sorted_list_head = current
        else:
            search_pointer = sorted_list_head
            while search_pointer.next is not None and current.value > search_pointer.next.value:
                search_pointer = search_pointer.next
            current.next = search_pointer.next
            search_pointer.next = current
        
    self.head = sorted_list_head
    temp = self.head
    while temp.next is not None:
        temp = temp.next
    self.tail = temp

def insertion_sort(self):

# Check if the length of the list is less than 2
    if self.length < 2:
        return
    
# Set the pointer to the first element of the sorted list
    sorted_list_head = self.head
    
# Set the pointer to the second element of the list
    unsorted_list_head = self.head.next
    
# Remove the first element from the sorted list
    sorted_list_head.next = None
    
# Iterate through the unsorted list
    while unsorted_list_head is not None:

# Save the current element
        current = unsorted_list_head
        
# Move the pointer to the next element in the unsorted list
        unsorted_list_head = unsorted_list_head.next
        
# Insert the current element into the sorted list
        if current.value < sorted_list_head.value:
            
# If the current element is smaller than the first element 
# in the sorted list, it becomes the new first element
            current.next = sorted_list_head
            sorted_list_head = current
        else:
            
# Otherwise, search for the appropriate position to insert the current element
            search_pointer = sorted_list_head
            while search_pointer.next is not None and current.value > search_pointer.next.value:
                search_pointer = search_pointer.next
            current.next = search_pointer.next
            search_pointer.next = current
    
# Update the head and tail of the list
    self.head = sorted_list_head
    temp = self.head
    while temp.next is not None:
        temp = temp.next
    self.tail = temp
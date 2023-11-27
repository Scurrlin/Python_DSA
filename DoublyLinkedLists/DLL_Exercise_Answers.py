# DLL: Constructor

class Node:
    def __init__(self, value):
        # Store node value
        self.value = value
        # Reference to next node
        self.next = None
        # Reference to previous node
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self, value):
        # Create new node with value
        new_node = Node(value)
        # Set head to new node
        self.head = new_node
        # Set tail to new node
        self.tail = new_node
        # Set initial length to 1
        self.length = 1

# DLL: Append

def append(self, value):
    # Create a new node with the given value
    new_node = Node(value)
    # Check if the list is empty (head is None)
    if self.head is None:
        # Set head and tail to the new node
        self.head = new_node
        self.tail = new_node
    else:
        # Connect the new node to the end of the list
        self.tail.next = new_node
        # Connect the new node to the previous node
        new_node.prev = self.tail
        # Update the tail to point to the new node
        self.tail = new_node
    # Increment the length of the list
    self.length += 1
    # Return True to indicate success
    return True

# DLL: Pop

# Define 'pop' method to remove last node in list
def pop(self):
    # Check if the list has no nodes
    if self.length == 0:
        # Return None to indicate an empty list
        return None
    
    # Store the tail node in 'temp' variable
    temp = self.tail
    
    # If list has just one node
    if self.length == 1:
        # Set head and tail to None, making list empty
        self.head = None
        self.tail = None
    else:
        # Set the tail to the node before the current tail
        self.tail = self.tail.prev
        # Remove link to last node by setting next to None
        self.tail.next = None
        # Detach the popped node from the list
        temp.prev = None
    
    # Decrement list length by 1 to reflect removal
    self.length -= 1
    
    # Return the removed node
    return temp

# DLL: Prepend
# DLL: Pop first
# DLL: Get
# DLL: Set
# DLL: Insert
# DLL: Remove

# All of the above actions don't have detailed explanations

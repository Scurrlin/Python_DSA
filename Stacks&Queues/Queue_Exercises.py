# FIFO - First In First Out

# Head in LL => First in Queue
# Tail in LL => Last in Queue

# Queue: Constructor

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    
    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

my_queue = Queue(4)

my_queue.print_queue()

# Queue: Enqueue

def enqueue(self, value):
    new_node = Node(value)
    if self.first is None:
        self.first = new_node
        self.last = new_node
    else:
        self.last.next = new_node
        self.last = new_node
    self.length += 1

my_queue = Queue(1)
my_queue.enqueue(2)

my_queue.print_queue()

# Queue: Dequeue

def dequeue(self):
    if self.length == 0:
        return None
    temp = self.first
    if self.length == 1:
        self.first = None
        self.last = None
    else:
        self.first = self.first.next
        temp.next = None
    self.length -= 1
    return temp

my_queue = Queue(1)
my_queue.enqueue(2)

# (2) Items - Returns 2 Node
print(my_queue.dequeue())
# (1) Items - Returns 1 Node
print(my_queue.dequeue())
# (0) Items - Returns None
print(my_queue.dequeue())


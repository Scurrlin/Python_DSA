# Stack: Push

def push(self, value):
    new_node = Node(value)
    if self.height == 0:
        self.top = new_node
    else:
        new_node.next = self.top
        self.top = new_node
    self.height += 1
    return True

# You can also simplify the code like this:

def push(self, value):
    new_node = Node(value)
    new_node.next = self.top
    self.top = new_node
    self.height += 1
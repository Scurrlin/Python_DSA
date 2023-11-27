# Stack: Implement Stack Using a List

class Stack:
    def __init__(self):
        self.stack_list = []

# Stack: Push for Stack That Uses a List

def push(self, value):
    self.stack_list.append(value)

# Stack: Pop for Stack That Uses a List

def pop(self):
    if self.is_empty():
        return None
    else:
        return self.stack_list.pop()

# Stack: Parentheses Balanced

def is_balanced_parentheses(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push(p)
        elif p == ')':
            if stack.is_empty() or stack.pop() != '(':
                return False
    return stack.is_empty()

def is_balanced_parentheses(parentheses):
    # Create a new stack
    stack = Stack()
 
    # Iterate over each character in the string
    for p in parentheses:
        # If the character is an opening parenthesis, 
        # push it onto the stack
        if p == '(':
            stack.push(p)
        # If the character is a closing parenthesis, 
        # pop the top element off the stack
        # and check if it matches the opening parenthesis
        elif p == ')':
            # If the stack is empty or the top element 
            # is not an opening parenthesis,
            # the parentheses are not balanced
            if stack.is_empty() or stack.pop() != '(':
                return False
 
    # If the stack is empty, the parentheses are balanced
    return stack.is_empty()

# Stack: Reverse String

def reverse_string(string):
    stack = Stack()
    reversed_string = ""
 
    for char in string:
        stack.push(char)
 
    while not stack.is_empty():
        reversed_string += stack.pop()
 
    return reversed_string

def reverse_string(string):
    # create a new stack
    stack = Stack() 
    # create an empty string to store the reversed string       
    reversed_string = ""   
 
    # push each character in the string onto the stack
    for char in string:
        stack.push(char)
 
    # pop each character off the stack and append it to the reversed string
    while not stack.is_empty():
        reversed_string += stack.pop()
 
    # return the reversed string
    return reversed_string

# Stack: Sort Stack

def sort_stack(stack):
    additional_stack = Stack()
 
    while not stack.is_empty():
        temp = stack.pop()
 
        while not additional_stack.is_empty() and additional_stack.peek() > temp:
            stack.push(additional_stack.pop())
 
        additional_stack.push(temp)
 
    while not additional_stack.is_empty():
        stack.push(additional_stack.pop())

def sort_stack(stack):
    # Create a new stack to hold the sorted elements
    additional_stack = Stack()
 
    # While the original stack is not empty
    while not stack.is_empty():
        # Remove the top element from the original stack
        temp = stack.pop()
 
        # While the additional stack is not empty and 
        #the top element is greater than the current element
        while not additional_stack.is_empty() and additional_stack.peek() > temp:
            # Move the top element from the additional stack to the original stack
            stack.push(additional_stack.pop())
 
        # Add the current element to the additional stack
        additional_stack.push(temp)
 
    # Copy the sorted elements from the additional stack to the original stack
    while not additional_stack.is_empty():
        stack.push(additional_stack.pop())

# Queue Using Stacks: Enqueue

def enqueue(self, value):
    while len(self.stack1) > 0:
        self.stack2.append(self.stack1.pop())
    self.stack1.append(value)
    while len(self.stack2) > 0:
        self.stack1.append(self.stack2.pop())

def enqueue(self, value):
    # Transfer all elements from stack1 to stack2
    while len(self.stack1) > 0:
        self.stack2.append(self.stack1.pop())
    
    # Add the new element to the bottom of stack1
    self.stack1.append(value)
    
    # Transfer all elements back from stack2 to stack1
    while len(self.stack2) > 0:
        self.stack1.append(self.stack2.pop())

# Queue Using Stacks: Dequeue

def dequeue(self):
    if self.is_empty():
        return None
    else:
        return self.stack1.pop()

def dequeue(self):
    # Check if the queue is empty
    if self.is_empty():
        # Return None if the queue is empty
        return None
    else:
        # Remove and return the last element in stack1
        # which is the first element in the queue
        return self.stack1.pop()
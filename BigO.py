# Big O: O(n)

def print_items (n):
    for i in range(n):
        print(i)

print_items(10)

# Big O: O(n) with explanation

def print_items(n):

# print_items accepts one argument 'n'. It will print
# a sequence of numbers from 0 up to, but not including, 'n'.
    
    for i in range(n):
        
# A for loop is initiated with 'i' iterating over
# the sequence of numbers produced by range(n).
# For each iteration, 'i' takes the current number in
# the sequence from 0 up to but not including 'n'.
        
        print(i)
        
# Inside the loop, print(i) is called. This prints
# the current value of 'i' to the console. This
# action is performed 'n' times due to the for loop,
# resulting in printing of numbers from 0 to 'n - 1'.

print_items(10)

# Big O: O(n) with multiple loops

def print_items(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)

print_items(10)

# Big O: O(n^2) with explanation

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
print_items(10)

def print_items(n):
    
# Start of the function that accepts 'n' as an argument.
 
    for i in range(n):
        
# Outer loop iterating over range 'n'.
# 'i' takes values from 0 to 'n-1'.
 
        for j in range(n):
            
# Inner loop iterating over range 'n'.
# 'j' takes values from 0 to 'n-1'.
 
            print(i,j)
            
# Prints the pair '(i, j)'.
# This happens 'n' times for each 'i', 
# printing all pairs where the first element 
# is 'i' and the second element is any number
# between '0' and 'n-1'.

print_items(10)

# Big O: Drop Non-Dominants

# This example shows O(n^2 + n)
# This is equivalent to 0(n^2) due to dropping the second, non-dominant code
# block

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
    
    for k in range(n):
        print(k)

print_items(10)

# Big O: O(1) => most efficient Big O

def add_items(n):
    return n + n + n + ...

# Big O: O(log n) => Divide and Conquer

# Big O: Different Terms for Inputs

# Top example is O(n)

def print_items(n):
    for i in range(n):
        print(i)
    
    for j in range(n):
        print(j)

# This next example is O(a + b) because there are multiple parameters
# O(a + b) cannot be simplified any further

def print_items(a, b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)

# This next example is 0(a * b) for similar reasons

def print_items(a, b):
    for i in range(a):
        for j in range(b):
            print(i,j)

# The reason that you use one data structure over another is almost always about
# Big O. 

# The reason that you would use a linked list over lists is because there are
# things that a linked list # can do more efficiently. For example, adding and
# removing from the beginning of a linked list is O(1) # while adding and
# removing from the beginning of a list is O(n).

# Think of data structures like a black box. You can put items in. You can take
# items out. If removing # the last item added quickly is your top priority and
# you have three choices which one would you choose?:

# 1) O(n)
# 2) O(log n)
# 3) O(1)

# It does not matter what data structure is in the black box, you know that you
# want the O(1) solution. # Here is what is in each black box:

# 1) O(n) Linked List
# 2) O(log n) Binary Search Tree
# 3) O(1) Lists or Doubly Linked List

# Now we have narrowed things down to two data structures. Let's say our second
# priority is removing items from the front of the list.  You have two options:

# 1) O(1)
# 2) O(n)

# Once again you want the O(1) option.  Now you have narrowed the proper data
# structure down to Doubly  # Linked Lists. It is going to be O(1) for both of
# your top priorities.

# Picking the best data structure is almost always about Big O.

# There will be other situations where knowing the relationships between items
# in the data structure is # important.  This is where a graph work better than
# anything and Big O will not give you the answer.

# But almost all of these types of interview questions are about Big O.
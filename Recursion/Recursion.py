# Recursion is a function that calls itself until it doesn't... lmao okay bro

# Pseudocode explaining gift box and ball analogy:

def open_gift_box():
    if ball:
        return ball
    open_gift_box()

# The process of opening each new box is the same
# Each time we open a box, we make the problem smaller
# When the function needs to call itself again, that is a "Recursive Case"
# When we open the gift box that has the ball in it, that is called the "Base Case"

# Recursion: Call Stack

def funcThree():
    print('Three')

def funcTwo():
    funcThree()
    print('Two')

def funcOne():
    funcTwo()
    print('One')

funcOne()

# Recursion: Factorial

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(4))
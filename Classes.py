# Classes

# "self" differentiates a method (part of a class) from a function
# "color" is the parameter

class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

cookie_one = Cookie('green')
cookie_two = Cookie('blue')

print('Cookie one is', cookie_one.get_color())
print('Cookie two is', cookie_two.get_color())

cookie_one.set_color('yellow')

print('\nCookie one is now', cookie_one.get_color())
print('Cookie two is still', cookie_two.get_color())

# "\n" is called the "new line character" and is used when printing
# "\n" when used in printing, prints the new information on a new line
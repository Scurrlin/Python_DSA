# Hash Tables

# Tables are dictionaries of key-value pairs
# Hashes are "one way" and "deterministic"

# Collisions occur when you put a key-value pair at an "address" that already
# contains a key-value pair

# The technique for dealing with collisions by simply authorizing two key-value
# pairs to occupy the same "address" is referred to as "Separate Chaining"

# Another way to deal with collisions is to parse through each indiviual address
# within the table until you find an unoccupied address. This is referred to as
# "Linear Probing"
# "Linear Probing" is a form of "open addressing"

# You can use Linked Lists to make Separate Chaining more efficient

# HT: Constructor

class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

my_hash_table = HashTable()

my_hash_table.print_table()

# HT: Set

def set_item(self, key, value):
    index = self.__hash(key)
    if self.data_map[index] == None:
        self.data_map[index] = []
    self.data_map[index].append([key, value])

my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

my_hash_table.print_table()

# HT: Get

def get_item(self, key):
    index = self.__hash(key)
    if self.data_map[index] is not None:
        for i in range(len(self.data_map[index])):
            if self.data_map[index][i][0] == key:
                return self.data_map[index][i][1]
    return None

my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)

print(my_hash_table.get_item('bolts'))
print(my_hash_table.get_item('washers'))
print(my_hash_table.get_item('lumber'))

# HT: Keys

def keys(self):
    all_keys = []
    for i in range(len(self.data_map)):
        if self.data_map[i] is not None:
            for j in range(len(self.data_map[i])):
                all_keys.append(self.data_map[i][j][0])
    return all_keys

my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

print(my_hash_table.keys())

# HT: Item in Common IQ (2 methods)

# Method 1 (not ideal)

def item_in_common(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

list1 = [1,3,5]
list2 = [2,4,5]

print(item_in_common(list1, list2))

# Method 2 (ideal)

def item_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True
    
    for j in list2:
        if j in my_dict:
            return True
    
    return False

list1 = [1,3,5]
list2 = [2,4,5]

print(item_in_common(list1, list2))

# HT: Sets

# Create a set using {}
my_set = {1, 2, 3, 4, 5}
 
# Create a set using set()
my_set = set([1, 2, 3, 4, 5])

# Add an element to a set
# If the number 6 is already in the set it will not be added again.
my_set.add(6)
 
# Update is used to add multiple elements to the set at once. 
# It takes an iterable object (e.g., list, tuple, set) as an 
# argument and adds all its elements to the set. 
# If any of the elements already exist in the set, 
# they are not added again.
my_set.update([3, 4, 5, 6])
 
# Removing an element from a set
my_set.remove(3)
 
# Union of two sets
other_set = {3, 4, 5, 6}
union_set = my_set.union(other_set)
 
# Intersection of two sets
intersection_set = my_set.intersection(other_set)
 
# Difference between two sets
difference_set = my_set.difference(other_set)
 
# Checking if an element is in a set
if "hello" in my_set:
    print("Found hello in my_set")
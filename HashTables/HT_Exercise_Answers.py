# HT: Constructor

def __init__(self, size = 7):
        self.data_map = [None] * size

# HT: Set

def set_item(self, key, value):
    # Compute the index in the hash table based on the key using the __hash method
    index = self.__hash(key)
    # If the bucket at the index is empty, initialize it to an empty list
    if self.data_map[index] == None:
        self.data_map[index] = []
    # Append the [key, value] pair to the bucket at the index
    self.data_map[index].append([key, value])

# HT: Get

def get_item(self, key):
    # get the index of the key in the hash table
    index = self.__hash(key)
    
    # check if there is any value stored in the index of the hash table
    if self.data_map[index] is not None:
        # iterate over the list of key-value pairs at the index
        for i in range(len(self.data_map[index])):
            # check if the key in the pair is the same as the one passed to the method
            if self.data_map[index][i][0] == key:
                # if so, return the value associated with the key
                return self.data_map[index][i][1]
    # if the key is not found in the hash table, return None
    return None

# HT: Keys

def keys(self):
    # list to store all the keys
    all_keys = []
    
    # iterate through each slot in the data map
    for i in range(len(self.data_map)):
        # if the slot is not empty, iterate through the items in the slot
        if self.data_map[i] is not None:
            for j in range(len(self.data_map[i])):
                # append the key to the list of keys
                all_keys.append(self.data_map[i][j][0])
    
    # return the list of keys
    return all_keys
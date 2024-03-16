# HT: Item in Common

def item_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True
 
    for j in list2:
        if j in my_dict:
            return True
 
    return False

def item_in_common(list1, list2):

# create an empty dictionary to store list1's values
    my_dict = {}
 
# iterate through list1 and add each value to the dictionary as a key
    for i in list1:
        my_dict[i] = True
 
# iterate through list2 and check if each value is a key in the dictionary
    for j in list2:

# if a value in list2 is also in the dictionary, return True
        if j in my_dict:
            return True
 
# if no values in common are found, return False
    return False

# HT: Find Duplicates

def find_duplicates(nums):
    num_counts = {}
    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1
    duplicates = [num for num, count in num_counts.items() if count > 1]
    return duplicates

def find_duplicates(nums):

# create an empty hash table
    num_counts = {}
 
# iterate through each number in the array
    for num in nums:

# add the number to the hash table or increment its count if it's already in the
# hash table
        num_counts[num] = num_counts.get(num, 0) + 1
 
# create a list of the numbers that appear more than once in the input array
    duplicates = [num for num, count in num_counts.items() if count > 1]
 
# return the list of duplicates
    return duplicates

# HT: First Non-Repeating Character

def first_non_repeating_char(string):
    char_counts = {}
    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char in string:
        if char_counts[char] == 1:
            return char
    return None

def first_non_repeating_char(string):

# create an empty hash table to count the frequency of each character
    char_counts = {}
    
# count the frequency of each character in the string
    for char in string:

# this increments the count by 1 in the dictionary
        char_counts[char] = char_counts.get(char, 0) + 1

# find the first non-repeating character in the string
    for char in string:
        if char_counts[char] == 1:
            return char

# return None if no non-repeating character is found
    return None

# HT: Group Anagrams

def group_anagrams(strings):
    anagram_groups = {}
    for string in strings:
        canonical = ''.join(sorted(string))
        if canonical in anagram_groups:
            anagram_groups[canonical].append(string)
        else:
            anagram_groups[canonical] = [string]
    return list(anagram_groups.values())

def group_anagrams(strings):

# create an empty hash table
    anagram_groups = {}
 
# iterate through each string in the array
    for string in strings:

# sort each string to get its canonical form
# sorted('eat') returns ['a', 'e', 't']
# ''.join(['a', 'e', 't']) coverts the array of chars to 'aet' string
        canonical = ''.join(sorted(string))
 
# check to see if the canonical form of the string exists in the hash table
        if canonical in anagram_groups:

# if it does then add the string there
            anagram_groups[canonical].append(string)
        else:

# otherwise create new canonical form and add the string there
            anagram_groups[canonical] = [string]
 
# convert the hash table to a list of lists
    return list(anagram_groups.values())

# HT: Two Sum

def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

def two_sum(nums, target):

# create an empty hash table
    num_map = {}
 
# iterate through each number in the array
    for i, num in enumerate(nums):
        
# calculate the complement of the current number
        complement = target - num
 
# check if the complement is in the hash table
        if complement in num_map:

# if it is, return the indices of the two numbers
            return [num_map[complement], i]
 
# add the current number and its index to the hash table
        num_map[num] = i
 
# if no two numbers add up to the target, return an empty list
    return []

# HT: Subarray Sum

def subarray_sum(nums, target):
    sum_index = {0: -1}
    current_sum = 0
    for i, num in enumerate(nums):
        current_sum += num
        if current_sum - target in sum_index:
            return [sum_index[current_sum - target] + 1, i]
        sum_index[current_sum] = i
    return []

def subarray_sum(nums, target):

# We create a dictionary called 'sum_index' to store 
# running sums (as keys) and their corresponding 
# indices in the array (as values).
#
# Why start with {0: -1}?
# - '0' will serve as the default sum when looking for subarrays.
# - '-1' indicates there's no subarray yet.
# This setup helps handle special cases, such as when the 
# first element itself is equal to the target.
    sum_index = {0: -1}
    
# Initialize a variable 'current_sum' to keep track of the 
# running sum as we iterate through the array.
    current_sum = 0
 
# The enumerate function allows us to loop through 'nums'
# while keeping track of both the index 'i' and the value 'num'.
    for i, num in enumerate(nums):

# Update 'current_sum' by adding the current element 'num'.
        current_sum += num
 
# We check if a subarray exists with a sum that equals the target.
# Specifically, we check if 'current_sum - target' is already
# a key in our 'sum_index' dictionary.
        if current_sum - target in sum_index:
            
# If it is, then we have found the subarray we are looking for.
# We return its start and end indices as a list.
#
# sum_index[current_sum - target] + 1 is the start index.
# We add 1 to move past the element before the subarray starts.
#
# 'i' is the end index, where the subarray ends.
            return [sum_index[current_sum - target] + 1, i]
 
# If we haven't yet found a subarray with the sum that matches
# the target, we add the 'current_sum' and its index 'i' to
# our 'sum_index' dictionary for future checks.
        sum_index[current_sum] = i
 
# If we've gone through the entire list and didn't find any
# subarray with a sum equal to the target, we return an empty list.
    return []

# HT Set: Remove Duplicates

def remove_duplicates(my_list):
    new_list = list(set(my_list)) 
    return new_list

def remove_duplicates(my_list): 

# Convert the list to a set and then back to a list to remove duplicates 
    new_list = list(set(my_list)) 
    return new_list

# HT Set: Has Unique Characters

def has_unique_chars(string):
    char_set = set()
    for char in string:
        if char in char_set:
            return False
        char_set.add(char)
    return True

def has_unique_chars(string):

# Create an empty set to store characters
    char_set = set()

# Loop through each character in the string
    for char in string:

# Check if the character is already in the set
        if char in char_set:

# If it is, return False (the string has duplicate characters)
            return False

# If the character is not in the set, add it to the set
        char_set.add(char)

# If we get to the end of the string without finding duplicates, return True
    return True

# HT Set: Find Pairs

def find_pairs(arr1, arr2, target):
    set1 = set(arr1)
    pairs = []
    for num in arr2:
        complement = target - num
        if complement in set1:
            pairs.append((complement, num))
    return pairs

def find_pairs(arr1, arr2, target):

# Convert arr1 to a set for O(1) lookup
    set1 = set(arr1)

# Initialize an empty list to store the pairs
    pairs = []

# Loop through each number in arr2
    for num in arr2:

# Calculate the complement of the current number
        complement = target - num

# Check if the complement is in set1
        if complement in set1:

# If it is, add the pair to the pairs list
            pairs.append((complement, num))

# Return the list of pairs that add up to the target value
    return pairs

# HT Set: Longest Consecutive Sequence

def longest_consecutive_sequence(nums):
    num_set = set(nums)
    longest_sequence = 0
    
    for num in nums:
        if num - 1 not in num_set:
            current_num = num
            current_sequence = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_sequence += 1
            
            longest_sequence = max(longest_sequence, current_sequence)
    
    return longest_sequence

def longest_consecutive_sequence(nums):

# Create a set to keep track of the numbers in the array
    num_set = set(nums)
    longest_sequence = 0
    
# Loop through the numbers in the nums array
    for num in nums:

# Check if the current number is the start of a new sequence
        if num - 1 not in num_set:
            current_num = num
            current_sequence = 1
            
# Keep incrementing the current number until the end of the sequence is reached
            while current_num + 1 in num_set:
                current_num += 1
                current_sequence += 1
            
# Update the longest sequence if the current sequence is longer
            longest_sequence = max(longest_sequence, current_sequence)
    return longest_sequence
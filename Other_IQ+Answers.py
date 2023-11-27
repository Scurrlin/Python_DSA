# List: Remove Element

def remove_element(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1
    return len(nums)

def remove_element(nums, val):
    # Initialize the index variable to 0
    i = 0
    
    # Iterate through the array using a while loop
    while i < len(nums):
        # Check if the current element is equal to the given value
        if nums[i] == val:
            # If equal, remove the element in-place using pop()
            nums.pop(i)
        else:
            # If not equal, increment the index to move to the next element
            i += 1
    
    # Return the new length of the modified array
    return len(nums)

# List: Find Max Min

def find_max_min(myList):
    maximum = minimum = myList[0]
    for num in myList:
        if num > maximum:
            maximum = num
        elif num < minimum:
            minimum = num
    return maximum, minimum

def find_max_min(myList):
    # Initialize the maximum and minimum variables 
    # to the first element of the list
    maximum = minimum = myList[0]
    
    # Traverse the list and update the 
    # maximum and minimum variables
    for num in myList:
        if num > maximum:
            maximum = num
        elif num < minimum:
            minimum = num
    
    # Return the maximum and minimum variables
    return maximum, minimum

# List: Find Longest String

def find_longest_string(string_list):
    longest_string = ""
    for string in string_list:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string

def find_longest_string(string_list):
    # Initialize the variable to store the longest string to an empty string
    longest_string = ""
    # Loop through each string in the list of strings
    for string in string_list:
        # Check if the length of the current string is greater than the
        # length of the current longest string
        if len(string) > len(longest_string):
            # If so, update the longest string to be the current string
            longest_string = string
    # Return the longest string
    return longest_string

# List: Remove Duplicates

def remove_duplicates(nums):
    if not nums:
        return 0
 
    write_pointer = 1
 
    for read_pointer in range(1, len(nums)):
        if nums[read_pointer] != nums[read_pointer - 1]:
            nums[write_pointer] = nums[read_pointer]
            write_pointer += 1
 
    return write_pointer

def remove_duplicates(nums):
    # Return 0 if input list is empty
    if not nums:
        return 0
 
    # Initialize write_pointer at index 1
    write_pointer = 1
 
    # Loop through list starting from index 1
    for read_pointer in range(1, len(nums)):
        # Check if current element is unique
        if nums[read_pointer] != nums[read_pointer - 1]:
            # Move unique element to write_pointer
            nums[write_pointer] = nums[read_pointer]
            # Increment write_pointer for next unique element
            write_pointer += 1
 
    # Return new length of list with unique elements
    return write_pointer

# List: Max Profit

def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
 
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
 
    return max_profit

def max_profit(prices):
    # Initialize min_price to positive infinity
    min_price = float('inf')
    # Initialize max_profit to 0
    max_profit = 0
 
    # Iterate through the list of stock prices
    for price in prices:
        # Update min_price with the lowest price so far
        min_price = min(min_price, price)
        # Calculate profit by selling at the current price
        profit = price - min_price
        # Update max_profit with the highest profit so far
        max_profit = max(max_profit, profit)
 
    # Return the maximum profit after iterating
    return max_profit

# List: Rotate

def rotate(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]

def rotate(nums, k):
    # Calculate the effective number of steps to rotate
    k = k % len(nums)
    # Rearrange the elements in the rotated order
    nums[:] = nums[-k:] + nums[:-k]

# List: Max Sub Array

def max_subarray(nums):
    if not nums:
        return 0
 
    max_sum = current_sum = nums[0]
 
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
 
    return max_sum

def max_subarray(nums):
    # Return 0 if input list is empty
    if not nums:
        return 0
 
    # Initialize max_sum and current_sum
    max_sum = current_sum = nums[0]
 
    # Iterate through the remaining elements
    for num in nums[1:]:
        # Update current_sum
        current_sum = max(num, current_sum + num)
        # Update max_sum if current_sum is larger
        max_sum = max(max_sum, current_sum)
 
    # Return the maximum subarray sum
    return max_sum
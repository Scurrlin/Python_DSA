# BS: Bubble Sort

def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0 ,-1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list

def bubble_sort(my_list):

# loop over the list n-1 times, where n is the length of the list
# starting from the end and going backwards
    for i in range(len(my_list) - 1, 0 ,-1):

# loop over each pair of adjacent elements up to i - 1
        for j in range(i):

# check if the current element is greater than the next element
            if my_list[j] > my_list[j+1]:
                
# if so, swap the elements using a temporary variable
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp

# return the sorted list
    return my_list

# BS: Selection Sort

def selection_sort(my_list):
    for i in range(len(my_list)-1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list

def selection_sort(my_list):

# loop over the list n-1 times, where n is the length of the list
    for i in range(len(my_list)-1):
        
# set the current index as the index of the smallest element
        min_index = i

# loop over each element in the unsorted part of the list
        for j in range(i+1, len(my_list)):

# if the current element is smaller than the current minimum, update the minimum index
            if my_list[j] < my_list[min_index]:
                min_index = j

# if the index of the minimum element is not i, swap the elements at indices i and min_index
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp

# return the sorted list
    return my_list

# BS: Insertion Sort

def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j] 
            my_list[j] = temp
            j -= 1
    return my_list

def insertion_sort(my_list):

# iterate over each element of the list starting from the second element
    for i in range(1, len(my_list)):

# store the current element being sorted in a temporary variable
        temp = my_list[i]

# iterate over the already sorted part of the list
        j = i-1

# while the current element is less than the previous element and the index is still in bounds
        while temp < my_list[j] and j > -1:

# swap the current element with the previous element
            my_list[j+1] = my_list[j] 
            my_list[j] = temp

# decrement the index j
            j -= 1

# return the sorted list
    return my_list
# QS: Pivot

def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
 
    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index

def pivot(my_list, pivot_index, end_index):

# initialize the swap index to the pivot index
    swap_index = pivot_index
 
# iterate over the list from the pivot index + 1 to the end index
    for i in range(pivot_index+1, end_index+1):
        
# if the current element is less than the pivot element
        if my_list[i] < my_list[pivot_index]:
            
# increment the swap index
            swap_index += 1
            
# swap the current element with the element at the swap index
            swap(my_list, swap_index, i)
    
# swap the pivot element with the element at the swap index
    swap(my_list, pivot_index, swap_index)
    
# return the index of the pivot element after swapping
    return swap_index

# QS: Quick Sort

def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index-1)  
        quick_sort_helper(my_list, pivot_index+1, right)       
    return my_list

def quick_sort_helper(my_list, left, right):
    
# check if there is more than one element in the sublist to be sorted
    if left < right:
        
# choose a pivot element and partition the list into two sublists
        pivot_index = pivot(my_list, left, right)
        
# recursively sort the left sublist (elements less than pivot)
        quick_sort_helper(my_list, left, pivot_index-1)
        
# recursively sort the right sublist (elements greater than or equal to pivot)
        quick_sort_helper(my_list, pivot_index+1, right)
    
# when there is only one element or no elements left to be sorted, return the sorted list
    return my_list
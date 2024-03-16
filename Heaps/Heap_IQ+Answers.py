# Heap: Kth Smallest Element in an Array

def find_kth_smallest(nums, k):
    max_heap = MaxHeap()
 
    for num in nums:
        max_heap.insert(num)
        if len(max_heap.heap) > k:
            max_heap.remove()
 
    return max_heap.remove()

def find_kth_smallest(nums, k):
    
# Initialize a new instance of MaxHeap
    max_heap = MaxHeap()
 
# Loop over each number in the input list
    for num in nums:
        
# Insert the current number into the heap.
 # The heap maintains its properties automatically
        max_heap.insert(num)
        
# If the heap size exceeds k, remove the maximum element.
# This keeps the heap size at k and ensures it only contains
# the smallest k numbers seen so far
        if len(max_heap.heap) > k:
            max_heap.remove()
 
# After the loop, the heap contains the smallest k numbers.
# The root of the heap is the kth smallest number,
# remove and return it as the function's result.
    return max_heap.remove()

# Heap: Maximum Element in a Stream

def stream_max(nums):
    max_heap = MaxHeap()
    max_stream = []
 
    for num in nums:
        max_heap.insert(num)
        max_stream.append(max_heap.heap[0])
 
    return max_stream

def stream_max(nums):
    
# Initialize an empty MaxHeap.
# This is a data structure where the parent node
# is always larger than or equal to its children.
    max_heap = MaxHeap()
    
# Initialize an empty list to store the maximum numbers 
# encountered so far while traversing the input list.
    max_stream = []
 
# Iterate over each number in the input list.
    for num in nums:
        
# Insert the current number into the MaxHeap.
# If this number is greater than the current maximum
# number in the heap, the heap will adjust itself
# so that this number becomes the new maximum
# (i.e., it moves to the root of the heap).
        max_heap.insert(num)
        
# After each insertion, append the maximum value in the heap
# to the max_stream list. This value is always at the root
# of the heap and can be accessed using max_heap.heap[0].
# As a result, max_stream[i] will always be the maximum value
# in nums up to index i.
        max_stream.append(max_heap.heap[0])
 
# After we've finished the loop, return the max_stream list.
# This list represents the maximum number encountered so far 
# for each position in the input list.
    return max_stream
# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        sorted_bondary = i
        smallest_index = sorted_bondary
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for unsorted_index in range(sorted_bondary, len(arr)):
            if arr[unsorted_index] < arr[smallest_index]:
                smallest_index = unsorted_index

        # TO-DO: swap
        # Your code here
        arr[smallest_index], arr[sorted_bondary] = arr[sorted_bondary], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    swaps_occurred = True
    while swaps_occurred:
        swaps_occurred = False

        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaps_occurred = True

    return arr
#     for i in range(0, unsorted_length -1):
#         if arr[i] > arr[i+1]:
#             arr[i], arr[i+1] = arr[i+1], arr[i]

#     if unsorted_length > 0:
#         bubble_sort(arr, unsorted_length - 1)

# # recurisve implementation of bubble sort

# arr = [4,3,67,34,29,30,2,15,6]

# bubble_sort(arr, len(arr))

# print(arr)


'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    # Your code here

    return arr

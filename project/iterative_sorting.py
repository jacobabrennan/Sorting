# Complete the selection_sort() function below in class with your instructor
def selection_sort(arr):
    arr_length = len(arr)
    for start_index in range(arr_length):
        swap_index = None
        for search_index in range(start_index, arr_length):
            if(swap_index is None):
                swap_index = search_index
                continue
            if(arr[search_index] < arr[swap_index]):
                swap_index = search_index
        arr[start_index], arr[swap_index] = arr[swap_index], arr[start_index]
    return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort(arr):
    for current in range(1, len(arr)):
        current_value = arr[current]
        swap = current
        for test_index in range(current-1, -1, -1):
            # End must be -1, instead of 0, as range stops /before/ End.
            if(arr[test_index] > current_value):
                swap = test_index
            else:
                break
        arr[swap+1:current+1], arr[swap] = arr[swap:current], arr[current]
    return arr


# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
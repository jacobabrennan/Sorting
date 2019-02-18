# STRETCH: implement Linear Search
def linear_search(arr, target):
    for index in range(arr):
        if(arr[index] is target):
            return index
    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):
    if(len(arr) == 0):
        return -1  # array empty
    low = 0
    high = len(arr)-1
    midpoint = int((high - low)/2 + low)
    while(low < high):
        test_value = arr[midpoint]
        if(test_value == target):
            return midpoint
        if(test_value < target):
            high = midpoint-1
            continue
        elif(test_value > target):
            low = midpoint+1
            continue
    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):
    if len(arr) == 0:
        return -1  # array empty
    middle = (low+high)/2
    test_value = arr[middle]
    if(test_value == target):
        return middle
    if(test_value > target):
        return binary_search_recursive(arr[middle+1:])
    if(test_value < target):
        return binary_search_recursive(arr[:middle+1])
    # If target cannot be compared to middle item, raise an exception
    raise Exception('Target cannot be compared to elements of array.')

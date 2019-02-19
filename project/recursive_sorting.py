# helper function
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a = 0
    b = 0
    # since arrA and arrB already sorted, we only need to compare the first
    # element of each when merging!
    for i in range(0, elements):
        if a >= len(arrA):
            # all elements in arrA have been merged
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            # all elements in arrB have been merged
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            # next element in arrA smaller, so add to final array
            merged_arr[i] = arrA[a]
            a += 1
        else:
            # else, next element in arrB must be smaller,
            # so add it to final array
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


# recursive sorting function
def merge_sort(arr):
    if len(arr) > 1:
        left = merge_sort(arr[0: int(len(arr) / 2)])
        right = merge_sort(arr[int(len(arr) / 2):])
        arr = merge(left, right)   # merge() defined later
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# TO-DO: implement the Quick Sort function below USING RECURSION
def quick_sort(arr, low, high):
    if(low >= high):
        return arr
    # Use high as pivot
    index_pivot = high
    index_low = low
    # Iterate over test cases, from case previous to high to lowest.
    value_pivot = arr[index_pivot]
    while(index_low < index_pivot):
        # Always test the value directly before pivot
        index_test = index_pivot-1
        value_test = arr[index_test]
        # If test is greater than pivot, swap them. Then Advance pivot index.
        if(value_test > value_pivot):
            arr[index_pivot], arr[index_test] = value_test, value_pivot
            index_pivot = index_test
        # Otherwise, swap test with low value. Then advance low index.
        else:
            value_low = arr[index_low]
            arr[index_low], arr[index_test] = value_test, value_low
            index_low += 1
    # Perform quick_sort on low and high halfs
    quick_sort(arr, low, index_pivot-1)
    quick_sort(arr, index_pivot+1, high)
    #
    return arr


# STRETCH: implement the Timsort function below
# hint: check out
# https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr

# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for num in range(cur_index, len(arr)):
            if arr[num] < arr[smallest_index]:
                smallest_index = num
        # TO-DO: swap
        if smallest_index != i:
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr

# TO-DO:  implement the Bubble Sort function below

def bubble_sort(arr):
    # loop through n-i elements
    for i in range(len(arr) - 1):
        for num in range(len(arr) - 1):
            if arr[num] > arr[num + 1]:
                arr[num], arr[num + 1] = arr[num + 1], arr[num]

    return arr

def bubble_sort_guided(arr):
    swaps_occured = True
    while swaps_occured:
        swaps_occured = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaps_occured = True
    return arr

print(bubble_sort_guided([5,2,8,7,3,4,6,1,9,0]))

# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr

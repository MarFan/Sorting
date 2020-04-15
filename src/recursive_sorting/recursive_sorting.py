# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    merged_arr = []
    # TO-DO
    pos = 0 # merged_arr postition
    i = 0
    j = 0

    while len(arrA) != 0 and len(arrB) != 0:
        if arrA[0] < arrB[0]:
            merged_arr.append(arrA[0])
            arrA.remove(arrA[0])
        else:
            merged_arr.append(arrB[0])
            arrB.remove(arrB[0])
    if len(arrA) == 0:
        merged_arr += arrB
    else:
        merged_arr += arrA

    # while i < len(arrA) and j < len(arrB):
    #     if arrA[i] < arrB[j]:
    #         merged_arr[pos] = arrA[i]
    #         i = i + 1
    #     else:
    #         merged_arr[pos] = arrB[j]
    #         j = j + 1
    #     pos += 1 # merged_arr position
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    if len(arr) <= 1:
        return arr
    
    # Initial split        
    lhs = arr[:len(arr) // 2]
    rhs = arr[len(arr) // 2:]

    left = merge_sort(lhs)
    right = merge_sort(rhs)
    
    return merge(left, right)

print(merge_sort([2,8,6,0,1,7,5,4,3,9]))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

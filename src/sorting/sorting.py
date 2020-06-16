# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    j, k = 0, 0
    for i in range(len(merged_arr)):
        if k > len(arrB) - 1:
            merged_arr[i] = arrA[j]
            j += 1
        elif j > len(arrA) - 1:
            merged_arr[i] = arrB[k]
            k += 1
        elif arrA[j] < arrB[k]:
            merged_arr[i] = arrA[j]
            j += 1
        elif arrB[k] < arrA[j]:
            merged_arr[i] = arrB[k]
            k += 1
    # Your code here
    return merged_arr
# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    arr = merge(left, right)
    return arr
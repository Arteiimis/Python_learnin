def QuickSort(arr, left = None, right = None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr) - 1 if not isinstance(right, (int, float)) else right
    if left < right:
        partition_index = Partition(arr, left, right)
        QuickSort(arr, left, partition_index - 1)
        QuickSort(arr, partition_index + 1, right)
    return arr

def Partition(arr, left, right):
    base = left
    index = base + 1
    i = index
    while i <= right:
        if arr[i] < arr[base]:
            swap(arr, i, index)
            index += 1
        i += 1
    swap(arr, base, index - 1)
    return index - 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

arr = [19, 30, 15, 54, 83, 21, 31, 52, 93, 74]
print(arr)
print(QuickSort(arr))
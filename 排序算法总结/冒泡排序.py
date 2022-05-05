def bubblesort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [19, 30, 15, 54, 83, 21, 31, 52, 93, 74]
print(arr)
print(bubblesort(arr))
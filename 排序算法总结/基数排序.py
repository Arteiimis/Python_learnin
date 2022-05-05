def radix_sort(arr):
    if not arr:
        return []
    max_num = max(arr)
    max_digit = len(str(abs(max_num)))
    
    dev = 1 
    mod = 10
    for i in range(max_digit):
        radix_quene = [list() for _ in range(mod * 2)]
        for j in range(len(arr)):
            radix = int(((arr[j] % mod) / dev) + mod)
            radix_quene[radix].append(arr[j])

        pos = 0
        for queue in radix_quene:
            for val in queue:
                arr[pos] = val
                pos += 1

        dev *= 10
        mod *= 10
    return arr

arr = [19, 30, 15, 54, 83, 21, 31, 52, 93, 74]
print(arr)
print(radix_sort(arr))
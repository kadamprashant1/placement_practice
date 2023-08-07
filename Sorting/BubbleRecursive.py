def sort(array, swaps, size):
    if swaps == 0:
        return array
    else:
        swap = 0
        for i in range(0, len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swap = 1
        return sort(array, swap, size-1)

print(sort([4,3,2,1,3],1,5))
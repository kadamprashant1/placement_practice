def shell_sort(arr):
    gap = len(arr) //2
    while gap >0:
        for i in range(gap, len(arr)):
            temp= arr[i]
            j = i
            while j>= gap and arr[j-gap] > temp:
                arr[j]= arr[j-gap]
                j = j -gap
            arr[j] = temp
        gap = gap //2
    return arr

arr = [27,34,5,6,23,6]
shell_sort(arr)
print(arr)

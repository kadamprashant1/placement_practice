def comb_sort(arr):
    n = len(arr)
    gap = n
    shrink = 1.3
    swapped = True

    while gap>1 or swapped:
        gap = int(gap/shrink)
        swapped=False
        i=0

        while i+ gap <n:
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
            i+=1
    return arr

list_a=[0.12,0.45,0.57,0.23,0.24]
print(comb_sort(list_a))
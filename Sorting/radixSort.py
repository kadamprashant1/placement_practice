def counting_sort(arr, place):
    size = len(arr)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        index = arr[i] // place
        count[index % 10] += 1

    for j in range(1, 10):
        count[j] += count[j - 1]

    k = size - 1
    while k >= 0:
        index = arr[k] // place
        output[count[index % 10] - 1] = arr[k]
        count[index % 10] -= 1
        k -= 1

    for a in range(0, size):
        arr[a] = output[a]


def radix_sort(arr):
    m = max(arr)
    place = 1
    while m // place > 0:
        counting_sort(arr, place)
        place *= 10


arr = [123, 243, 125, 23, 62, 342, 125]
radix_sort(arr)
print(arr)

def counting_sort(list_a):
    size = len(list_a)
    output = [0] * size

    # Find the maximum value in the list
    max_value = max(list_a)

    # Create a count list with a size equal to max_value + 1
    count = [0] * (max_value + 1)

    # Count the occurrences of each element
    for i in range(size):
        count[list_a[i]] += 1

    # Calculate the cumulative count
    for j in range(1, max_value + 1):
        count[j] += count[j-1]

    # Place the elements in the sorted order
    for k in range(size - 1, -1, -1):
        output[count[list_a[k]] - 1] = list_a[k]
        count[list_a[k]] -= 1

    # Copy the sorted elements back to the original list
    for i in range(size):
        list_a[i] = output[i]

li = [2, 4, 6, 5, 3, 2, 4, 2]
counting_sort(li)
print(li)

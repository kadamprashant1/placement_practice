def bucket_sort(list_l):
    bucket = [[] for _ in range(len(list_l))]  # Create an empty bucket for each element in the input list
    for j in list_l:
        index = int(10 * j)  # Determine the index of the bucket where the current element should be placed
        bucket[index].append(j)  # Add the element to the corresponding bucket
    for k in range(len(list_l)):
        bucket[k] = sorted(bucket[k])  # Sort each bucket individually
    a = 0
    for b in range(len(list_l)):
        for c in range(len(bucket[b])):
            list_l[a] = bucket[b][c]  # Move the elements from the buckets back to the input list
            a += 1
    return list_l

li = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
test = bucket_sort(li)
print(test)

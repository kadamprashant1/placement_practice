def n_permutation(arr):#fucation called by passing array
    index = -1 #used to track index of array
    n = len(arr)
    for i in range(n - 2, 0, -1): #array iterate from n-2 to 0th index
        if arr[i] < arr[i + 1]: #basically it find beck point of array
            index = i # store beck points address
            break
    if index == -1:
        arr.reverse() # if it doesn't find break point then reverse the array
    for j in range(n - 1, index, -1):
        if arr[j] > arr[index]: #swap the element at index and greater than index
            arr[j], arr[index] = arr[index], arr[j]
    return arr


arr = [1, 2, 3,4,2,1] # here is need to Find next permutaion of numbers of array
print(n_permutation(arr))



# 1 2 3 5 3 2 1
#       -
#       |  
#    -  | -  
#  -    |   -
#-      |      -
#       |
# break ^ point
#       ^

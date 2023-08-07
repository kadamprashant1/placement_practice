# this problem is about count the condition of 
# i< j and arr[i] > arr[j]
## first approch using 2 pointer i & j with O(n^2)
## next approch is by using merger sort 
## count the inversion while merging the array
#complexity becomes O(nlogn)
def mergeSort(arr, left, right):
    mid =0
    inv_count =0
    if left < right:
        mid = (left+right) // 2

        #recursive seeing inversion pairs on left child
        inv_count += mergeSort(arr, left, mid)

        #recursively seeing the inversion pairs on right child
        inv_count += mergeSort(arr, mid+1, right)

        #Finding inversion pairs in merging operation
        inv_count += merge(arr,left, mid, right)

    return inv_count

def merge(arr, left, mid, right):
    temp_arr = []
    i = left
    j = mid +1
    inv_count = 0

    while i<= mid and j <= right :
        #if arr[i] <= arr[j] then its not an inversion pair
        if arr[i] <= arr[j]:
            temp_arr.append(arr[i])
            i+=1
        else:
            #if arr[i] > arr[j] then its inversion pair and arr[j] is inversion
            #pair with all elements from i to end of first sub array(i.e. mid)
            temp_arr.append(arr[j])
            inv_count += mid - i+1
            j+=1

    #completing the array if some elements are left out
    
    while i <= mid:
        temp_arr.append(arr[i])
        i+=1
    while j<=right:
        temp_arr.append(arr[j])
        j+=1
    #transferring this back to the original array
    for i in range(left, right+1):
        arr[i] = temp_arr[i-left]
    return inv_count



arr = [99 , 80 , 23 , 4]
print(mergeSort(arr, 0,len(arr)-1))
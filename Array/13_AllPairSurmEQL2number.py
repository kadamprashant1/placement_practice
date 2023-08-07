

def pairsum_sorted_array(arr,k):#for sorted array
    i=0
    n=len(arr)
    j=n-1
    count=0
    while i<j:
        if arr[i]+arr[j]==k:
            count+=1
            i+=1
            j-=1
        elif arr[i]+arr[j] >k:
            j-=1
        else:
            i+=1
    if count==0:
        return -1
    return count

def pairsum_non_sorted_array(arr,k):
    i=0


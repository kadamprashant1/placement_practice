def rotate_by_K(arr,k):
    k = k % len(arr) 
    print(arr[k:] + arr[:k]) 
if __name__=="__main__":
    k = int(input("Enter value for k"))
    arr = input("Enter array")
    arr = list(map(int,arr.split()))
    rotate_by_K(arr, k)
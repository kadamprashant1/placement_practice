def find_k_smallest(arr,k):
    if k >= len(arr):
        print("wrong intput")
        return
    else:
        arr.sort()
        print(arr[k-1])
        return 
if __name__== "__main__":
    k = int(input("Inter kth smallest element:"))
    n = input()
    arr = list(map(int,n.split()))
    find_k_smallest(arr,k)
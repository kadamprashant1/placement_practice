def acc_decc(arr):
    n = len(arr)
    arr[n//2:] =sorted(arr[n//2:])
    arr[n//2:]= sorted(arr[n//2:],reverse=True)
    print(arr)
    return
if __name__=="__main__":
    arr = input()
    arr = list(map(int,arr.split()))
    acc_decc(arr)
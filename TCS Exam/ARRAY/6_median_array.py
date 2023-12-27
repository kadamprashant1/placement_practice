
def find_med(arr):
    arr.sort()
    n =len(arr)
    if n % 2== 0:
        print((arr[n//2 -1] + arr[(n//2 )])/2)
    else:
        print(arr[n//2])
    return
if __name__=="__main__":
    arr = input()
    arr = list(map(int,arr.split()))
    find_med(arr)
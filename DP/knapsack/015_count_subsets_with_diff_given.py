#Input array= [1,1,2,3] diff= 1
#return no. which give number of partitions

def count_of_subset(arr,arr_sum):
    t=[[0 for i in range(arr_sum+1)]for j in range(len(arr)+1)]
    for i in range(len(arr) +1):
        t[i][0]=1
    for i in range(1,len(arr)+1):
        for j in range(1,arr_sum+1):
            if arr[i-1]<=j:
                t[i][j]=t[i-1][j]+t[i-1][j-arr[i-1]]
            else:
                t[i][j]=t[i -1][j]
    return t[len(arr)][arr_sum]


if __name__=="__main__":
    array=[1,1,2,3]
    diff=1
    n=len(array)
    full_sum=sum(array)
    arr_sum=(diff + full_sum)//2
    print("no. of all subset with diff : " + str(count_of_subset(array,arr_sum)))

    
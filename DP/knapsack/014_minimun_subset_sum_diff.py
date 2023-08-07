#Input array
# find minimun subset sum difference



def subset(n, k, arr):
    dp = [[False for j in range(k+1)] for i in range(n+1)]
    for i in range(n+1):
        dp[i][0] = True

    for i in range(1,n+1):
        for j in range(1,k+1):

            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][:(k//2)+1]

def minSubsetSumDifference(arr, n):

    min_num = float("inf")
    total = sum(arr)
    number_list = subset(n, total, arr)

    for inx,num in enumerate(number_list):
        if num:
            min_num = min(min_num,total-(inx*2))
    return min_num

if __name__=="__main__":
    array=[1,6,11,5]
    n=len(array)
    print(minSubsetSumDifference(array,n))
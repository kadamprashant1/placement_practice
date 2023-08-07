


if __name__ == "__main__":
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    W = 50
    n = len(profit)
    # intialized
    t = [[0 for i in range(W+1)] for j in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,W+1):
            if(weight[i-1]<=j):
                t[i][j]= max(profit[i-1] + t[i-1][j-weight[i-1]], t[i-1][j])
            else:
                t[i][j]=t[i-1][j]
    print(t[n][W])



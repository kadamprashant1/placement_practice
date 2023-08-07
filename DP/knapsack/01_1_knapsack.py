


def knapSack(W, weight, profit, n):
    if W == 0 or n == 0:
        return 0
    if t[n][W]!= -1:
        return t[n][W]
    
    if weight[n - 1] <= W:
        t[n][W]= max(
            profit[n - 1] + knapSack(W - weight[n - 1], weight, profit, n - 1),
            knapSack(W, weight, profit, n - 1)
        )
        return t[n][W]
    else:
        t[n][W]= knapSack(W, weight, profit, n - 1)
        return t[n][W]


if __name__ == "__main__":
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    W = 50
    n = len(profit)
    t = [[-1 for i in range(W+1)] for j in range(n+1)]
    print(knapSack(W, weight, profit, n))

def knapSack(W, weight, profit, n):
    if W == 0 or n == 0:
        return 0
    if weight[n - 1] <= W:
        return max(
            profit[n - 1] + knapSack(W - weight[n - 1], weight, profit, n - 1),
            knapSack(W, weight, profit, n - 1)
        )
    else:
        return knapSack(W, weight, profit, n - 1)


if __name__ == "__main__":
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    W = 50
    n = len(profit)
    print(knapSack(W, weight, profit, n))

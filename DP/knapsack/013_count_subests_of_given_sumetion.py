# Input arr[]= 2 3 5 6 8 10
# sum = 10
# here is OUTPUT is given by int type which is nu. of all possible subsets

if __name__ == "__main__":
    arr = [2, 3, 5, 6, 8, 10]
    target_sum = 10
    n = len(arr)
    t = [[0 for i in range(target_sum + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        t[i][0] = 1
    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j] + t[i - 1][j - arr[i - 1]]
            else:
                t[i][j] = t[i - 1][j]
    print("Number of possible subsets having sum = " + str(target_sum) + " are " + str(t[n][target_sum]))


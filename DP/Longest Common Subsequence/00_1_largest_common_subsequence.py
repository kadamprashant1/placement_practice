# input x="abcdgh"
#       y="abedhr"  return number of largest common subsequence
# bottom up dp code

def lcs(x, y, n, m):
    if n == 0 or m == 0:
        return 0
    if t[n][m] != -1:
        return t[n][m]
    if x[n - 1] == y[m - 1]:
        t[n][m] = 1 + lcs(x, y, n - 1, m - 1)
        return t[n][m]
    else:
        t[n][m] = max(lcs(x, y, n - 1, m), lcs(x, y, n, m - 1))
        return t[n][m]


if __name__ == "__main__":
    x = "abcdgh"
    y = "abedhr"
    n = len(x)
    m = len(y)
    t = [[-1 for i in range(m + 1)] for j in range(n + 1)]
    print("The length of the longest common subsequence is: " + str(lcs(x, y, n, m)))

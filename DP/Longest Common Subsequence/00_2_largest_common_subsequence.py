

if __name__ == "__main__":
    x = "abcdgh"
    y = "abedhr"
    n = len(x)
    m = len(y)
    t = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if (x[i-1]==y[j-1]):
                t[i][j]=1+t[i-1][j-1]
            else:
                t[i][j]=max(t[i-1][j-1], t[i][j-1])
    print("The length of the longest common subsequence is: " + str(t[n][m]))
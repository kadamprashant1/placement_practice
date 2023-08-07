#coin =[1,2,3]  sum =5
#find th way to find target using unlimited coin from given set of coins

if __name__=="__main__":
    coin =[1,2,3]  
    sum_ =5
    n=len(coin)
    t=([[0 for i in range(sum_ + 1)]for j in range(n+1)])
    for i in range(n+1):
        t[i][0]=1
    
    for i in range(1,n+1):
        for j in range(1,sum_+1):
            if coin[i-1]<=j:
                t[i][j]=t[i][j-coin[i-1]] + t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    print("ways to find target sum using unlimited coin is : " + str(t[n][sum_]))



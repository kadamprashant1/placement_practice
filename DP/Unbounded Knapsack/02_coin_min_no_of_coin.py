#Input coin =[1,2,3]  t_sum = 5



if __name__=="__main__":
    coin =[1,2,3]  
    t_sum = 5
    n=len(coin)
    # initialize .................>
    t=([[0 for i in range(t_sum+1)] for j in range(n +1)])
    # first row .......................>
    for i in range(t_sum+1):
        t[0][i]=float("inf")-1
    # second row .....................>
    for j in range(1,t_sum+1):
        if ((j%coin[0])== 0):
            t[1][j]=j//coin[0]
        else:
            t[1][j]=float("inf") -1
    #code starts from third row
    for i in range(2,n+1):
        for j in range(t_sum+1):
            if coin[i-1]<=j:
                t[i][j]=min(t[i][j -coin[i-1]] +1, t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    print("min no. of coint is : " + str(t[n][t_sum]))
        
    
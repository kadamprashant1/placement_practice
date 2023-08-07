# Input array []= 2 3 7 8 10
# target Sum = 11
# using Top - Down approach
# return True or False

if __name__=="__main__":
    array=[2,3,7,8,10]
    sum = 11
    n = len(array)
    t =([[False for i in range(sum + 1)]for i in range(n + 1)])
    
    #intialization ......................................<>
    for i in range(sum +1):
        t[0][i] = False
    for j in range(n+1):
        t[j][0]=True    
    #....................................................</>
    # dp code............................................>
    for i in range(1,len(array)+1):
        for j in range(1,sum+1):
            if(array[i-1] <=j):
                t[i][j]= t[i][j-array[i-1]] or t[i-1][j]
            else:
                t[i][j] =t[i-1][j]
    #....................................................</>
    print(" it is possible to get target sum : " + str(t[len(array)][sum]) )
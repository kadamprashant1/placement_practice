#Input a:"abcde"
#      b:"abfce" output 2

if __name__=="__main__":
    a="abcde"
    b="abfce"
    n=len(a)
    m=len(b)
    max_=float("-inf")
    t=[[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if (a[i-1] == b[i-1]):
                t[i][j]=t[i-1][j-1] +1
            else:
                t[i][j]=0
   
    for i in range(1,n+1):
        if(t[i][m]>max_):
            max_=t[i][m]
    print("longest substring is : "+ str(max_))

        
            
           



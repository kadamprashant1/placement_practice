# input x="abcdgh"
#       y="abedhr"  return number of largest common subsequence
# recursive code
def lcs(x,y,n,m):
    if(n==0 or m==0):
        return 0
    if(x[n-1]==y[m-1]):
        return lcs(x,y,n-1,m-1) +1
    else:
        return max(lcs(x,y,n-1,m), lcs(x,y,n,m-1))

if __name__=="__main__":
    x="abcdgh"
    y="abedhr" 
    n=len(x)
    m=len(y)
    print("here is length of largest common subsequence is : "+ str(lcs(x,y,n,m)))

class rectangle:
    def print_HollowRectangle(self,n,m):
        if n<=0:
            print("Enter a valid value")
        else:
            for i in range(1,n+1):
                for j in range(1,m+1):
                    if i==1 or i==n or j==1 or j==m:
                        print("*",end="")
                    else:
                        print(" ",end="")
                print("")


s=rectangle()
s.print_HollowRectangle(4,5)
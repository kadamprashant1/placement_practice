class solution:
    def pyramidStar(self,n):
        if(n<=0):
            print("Enter valid Number")
        else:
            k=n-1
            for i in range(n):
                for j in range(0,k):
                    print(end=" ")
                k=k-1
                for j in range(0,i+1):
                    print("* ",end="")
                print("\r")
               
s=solution()
s.pyramidStar(5)
class solution:
    def rightPyramid(self,n):
        for i in range(n+1):
            for j in range(i):
                print("* ",end="")
            print("\r")
        
    def leftPyramid(self,n):
        k=1
        for i in range(n,-1,-1):
            for j in range(i):
                print("* ",end="")
            print("\r")

if __name__=="__main__":
    s=solution()
    s.rightPyramid(5)
    s.leftPyramid(5)
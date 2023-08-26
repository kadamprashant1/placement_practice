def NearestGreatertoRight(a,n):
    stack=[]
    ans=[]
    for i in range(n-1,-1,-1):
        while stack and a[i]>stack[-1]:
            stack.pop()
        if not stack:
            ans.append(-1)
        else:
            ans.append(stack[-1])
        stack.append(a[i])
    ans.reverse()
    return ans
def main():
    a = [4, 5, 2, 10, 8]
    n = len(a)

    result = NearestGreatertoRight(a, n)
    print("Next larger elements for the input array:", a)
    print("Result:", result)
if __name__=="__main__":
    main()
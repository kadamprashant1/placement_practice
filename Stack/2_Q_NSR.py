def Nsr(array, size):
    stack=[]
    ans=[]
    for i in range(size-1,-1,-1):
        while stack and array[i] < stack[-1]:
            stack.pop()
        if not stack:
            ans.append(-1)
        else:
            ans.append(stack[-1])
        stack.append(array[i])
    ans.reverse()
    return ans

if __name__=="__main__":
    array = [87,62, 94, 61 ,12, 74, 96, 23, 34]
    size = len(array)
    result = Nsr(array, size)
    print("Next smaller to right elements for the input array:", array)
    print("Result:", result)
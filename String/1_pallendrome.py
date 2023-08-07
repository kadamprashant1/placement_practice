def pallendrome(string):
    n = len(string)
    for i in range(0, n // 2):
        if string[i] != string[n - i - 1]:
            return False
    return True

def stack_pallendrome(string):
    if string == "":
        return False
    n = len(string)
    stack = []
    for i in range(0, n // 2):
        
        stack.append(string[i])
    for i in range(n // 2, n):
     
        if stack.pop() == string[i]:
            i =1
    if len(stack)==0:
        return True



    

print(pallendrome("aaaaw"))
print(stack_pallendrome("aaaaw"))

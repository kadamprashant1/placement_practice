def rev(string):#O(n) time and O(1) spcae using loop
    str = ""#empty string
    for i in string:#
        str = i + str
    return str
#//////////////////////////////////////////////////////////////////////////
def rev1(string): # using a recursion
    if len(string)==0:
        return string
    else:
        return rev1(string[1:]) +string[0]
 #//////////////////////////////////////////////////////////////////////////   
def rev2(string):#O(n) time and O(n) space using stack 
    stack=[]
    n=len(string)
    for i in string:
        stack.append(i)
    rev_string = ""
    for i in range(0,n , 1):
        rev_string += stack.pop()
    return rev_string
#//////////////////////////////////////////////////////////////////////////
def rev3(string):#O(n) time and O(1) space extended slice
    string = string[::-1]
    return string
#//////////////////////////////////////////////////////////////////////////

def rev4(string):#O(n) time and O(n)space using reversed 
    string = "".join(reversed(string))
    return string
#//////////////////////////////////////////////////////////////////////////
def rev5(string):# O(n)time and O(1) space using list comprehenstion()
    string = [string[i] for i in range(len(string)-1,-1,-1)]
    return "".join(string)
#//////////////////////////////////////////////////////////////////////////
def rev6(string):#O(n) time and O(1) space using fucntion call
    string = list(string)
    string.reverse()
    return "".join(string)
 #//////////////////////////////////////////////////////////////////////////


string =" hello world !"
print(rev(string))
print(rev1(string))
print(rev2(string))
print(rev3(string))
print(rev4(string))
print(rev5(string))
print(rev6(string))
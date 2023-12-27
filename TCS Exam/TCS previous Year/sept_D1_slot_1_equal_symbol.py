# Problem Statement – Given a string S(input consisting) of ‘*’ and ‘#’. The length of the string is variable. The task is to find the minimum number of ‘*’ or ‘#’ to make it a valid string. The string is considered valid if the number of ‘*’ and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
# Note : The output will be a positive or negative integer based on number of ‘*’ and ‘#’ in the input string.

# (*>#): positive integer
# (#>*): negative integer
# (#=*): 0
# Example 1:
# Input 1:

# ###***   -> Value of S
# Output :

# 0   → number of * and # are equal

def check_equl(strng):
    dict={}
    for i in strng:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    if dict['*']==dict['#']:
        print(0)
    elif dict['#']>dict['*']:
        print(-1)
    else:
        print(1)
if __name__=="__main__":
    strng = input()
    check_equl(strng)
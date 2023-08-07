#1st brute force approach

#2nd using s3=s1+s1
def check_rotated(original,rotated):
    if len(original)==len(rotated):
        bigstring =original + original
        for i in range(0,len(bigstring)//2):
            if bigstring[i]==rotated[0]:
                for j in range(0,len(rotated)):
                    if bigstring[i+j]!=rotated[j]:
                        return False
        return True
    else:
        return False

if __name__=='__main__':
    original="prashant"
    rotated="rashantp"
    print("string is rotated = ",end="")
    print(check_rotated(original,rotated))

                        
    
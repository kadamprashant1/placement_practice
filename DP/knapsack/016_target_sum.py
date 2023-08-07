#Input arr=[1,1,2,3]  sum = 3
#find the all arthmatic combination of array to get sum as = sum

#might wrong

def partition_sum(array,sum):
    t=([[0 for i in range(sum +1)]for j in range(len(array) +1)])
    for i in range(len(array) +1):
        t[i][0]=1
    for i in range(1,len(array) +1):
        for j in range(1,sum+1):
            if(array[i-1] <=j):
                t[i][j]=t[i-1][j] + t[i][j-array[i-1]]
            else:
                t[i][j]=t[i-1][j]
    return t[i][j]

if __name__ == "__main__":
    array=[1,1,2,3]
    t_sum= 1
    f_sum=sum(array)
    t_sum=(f_sum+t_sum)//2
    print("no. of partition are : "+ str(partition_sum(array,t_sum)))
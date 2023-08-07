from sortedcontainers import SortedDict
import math


def median_f(matrix):
    n=len(matrix)
    m=len(matrix[0])
    my_dic =SortedDict()
    key=0
    for i in range(0,n):
        for j in range(0,m):
            my_dic[matrix[i][j]]+=1
            key+=1

    if key//2!=0:
        return my_dic[math.ceil(key//2)]
    else:
        mid = key//2
        return ((my_dic[mid] + my_dic[mid+1])//2)

m = [[1, 3, 5], 
     [2, 6, 9], 
     [3, 6, 9]]
print(median_f(m))
# length = [1,2,3,4,5,6,7,8] price=[1,5,8,9,11,17,17,20] lenth_road= 8

if __name__=="__main__":
    length = [1,2,3,4,5,6,7,8] 
    price=[1,5,8,9,11,17,17,20] 
    lenth_road= 8
    t=([[0 for i in range(len(length)+1)] for j in range(len(price) +1)])
    for i in range(len(length) +1):
        for j in range(len(price)+1):
            if length[i-1] <=j:
                t[i][j]= max(price[i-1] + t[i][j-length[i-1]], t[i-1][j])
            else:
                t[i][j]= t[i-1][j]
    print(t[len(price)][len(length)])
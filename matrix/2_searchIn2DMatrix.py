#aproch 1:- Brute force is using linear search O(N^2)

#approach 3: using strait forword strait to ans algo

def search_matrix(matrix, search):
    i=0
    j=len(matrix[0]) -1
    n=len(matrix) 
    m=len(matrix[0]) 

    while (i>=0 and i<n) and (j>=0 and j<m):
        if matrix[i][j]==search:
            return 1
        elif matrix[i][j]>search:
            j-=1
        elif matrix[i][j]<search:
            i+=1
    return -1





#aproach 2:- can go for binary search
#//////////////////////////////////
# def search_matrix(matrix, search):
#     rows = len(matrix)
#     cols = len(matrix[0])

#     left = 0
#     right = rows * cols - 1

#     while left <= right:
#         mid = (left + right) // 2
#         mid_value = matrix[mid // cols][mid % cols]

#         if mid_value == search:
#             return 1
#         elif mid_value < search:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return 0

#///////////////////////////////////////

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
search = 9
print(search_matrix(matrix, search))

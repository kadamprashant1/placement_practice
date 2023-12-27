# A parking lot in a mall has RxC number of parking spaces. Each parking space will either be  empty(0) or full(1). The status (0/1) of a parking space is represented as the element of the matrix. The task is to find index of the prpeinzta row(R) in the parking lot that has the most of the parking spaces full(1).

# Note :
# RxC- Size of the matrix
# Elements of the matrix M should be only 0 or 1.

# Example 1:
# Input :
# 3   -> Value of R(row)
# 3    -> value of C(column)
# [0 1 0
#  1 1 0 
#  1 1 1] -> Elements of the array M[R][C] where each element is separated by new line.
# Output :
# 3  -> Row 3 has maximum number of 1’s

# Example 2:
# input :
# 4 -> Value of R(row)
# 3 -> Value of C(column)
# [0 1 0 1 1 0 1 0 1 1 1 1] -> Elements of the array M[R][C]
# Output :
# 4  -> Row 4 has maximum number of 1’s
# ----------------------------------------------------------solution--------------------------------------------------------

if __name__ == "__main__":
    row = int(input("Enter the number of rows: "))
    col = int(input("Enter the number of columns: "))
    arr_input = input("Enter space-separated values: ")
    arr = list(map(int, arr_input.split()))

    k = 0
    ans = []


    for i in range(row):
        ans.append([])

    for i in range(row):
        for j in range(col):
            ans[i].append(arr[k])
            k += 1

    for i in range(row):
        ans[i][0] = sum(ans[i])

    max_row = max(ans, key=lambda x: x[0])
    print("Row with the maximum sum:", max_row[0])

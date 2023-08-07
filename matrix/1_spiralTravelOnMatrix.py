#their only one optimal printing method is available for it

def print_matrix(arr):
    top = 0
    output = []
    right = len(arr[0]) - 1
    bottom = len(arr) - 1
    left = 0

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            output.append(arr[top][i])
        top += 1

        for j in range(top, bottom + 1):
            output.append(arr[j][right])
        right -= 1

        for k in range(right, left - 1, -1):
            output.append(arr[bottom][k])
        bottom -= 1

        for i in range(bottom, top - 1, -1):
            output.append(arr[i][left])
        left += 1

    print(' '.join(map(str, output)))


matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11,12]]

print_matrix(matrix)

# Input arr[] = 1 5 11 5
# find if possible to devide this array into two equal partition sum
# output in True or False

def subset_sum(array, full_sum):
    check = check_even(full_sum)
    if not check:
        return False
    
    for i in range(1, len(array) + 1):
        for j in range(1, full_sum + 1):
            if array[i - 1] <= j:
                t[i][j] = t[i][j - array[i - 1]] or t[i - 1][j]
            else:
                t[i][j] = t[i - 1][j]
    
    return t[len(array)][full_sum]


def check_even(full_sum):
    if full_sum % 2 == 0:
        return True
    return False


if __name__ == "__main__":
    array = [1, 5, 11, 5]
    n = len(array)
    full_sum = sum(array)
    
    # Initialization
    t = [[False for i in range(full_sum + 1)] for j in range(n + 1)]
    for i in range(full_sum + 1):
        t[0][i] = False
    for j in range(n + 1):
        t[j][0] = True
    
    print("Partition is possible: " + str(subset_sum(array, full_sum // 2)))

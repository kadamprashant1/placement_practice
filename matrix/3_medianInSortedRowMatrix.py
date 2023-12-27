def median_f(matrix):
    flattened = [element for row in matrix for element in row]
    sorted_flattened = sorted(flattened)

    total_elements = len(sorted_flattened)
    mid = total_elements // 2

    if total_elements % 2 != 0:
        return sorted_flattened[mid]
    else:
        return (sorted_flattened[mid - 1] + sorted_flattened[mid]) // 2

m = [
    [1, 3, 5],
    [2, 6, 9],
    [3, 6, 9]
]

print(median_f(m))

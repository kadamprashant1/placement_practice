def print_center_aligned_pyramid(rows):
    for i in range(rows):
        print(" " * (rows - i - 1), end='')  # Print spaces for center alignment

        # Calculate and print the numbers for each row
        num = 1
        for j in range(i + 1):
            print(f"{num:^4}", end='')  # Center-align and print the number
            num = num * (i - j) // (j + 1)  # Calculate the next number
        print()  # Move to the next line

#rows = int(input("Enter the number of rows for the pyramid: "))
print_center_aligned_pyramid(5)

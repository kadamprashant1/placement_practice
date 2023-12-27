def cal_mean(data):
    return sum(data) / len(data)

def cal_slope(x, y, x_mean, y_mean):
    numerator = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(len(x)))
    denominator = sum((x[i] - x_mean) ** 2 for i in range(len(x)))

    if denominator != 0:
        return numerator / denominator
    else:
        # Handle the case where the denominator is zero (avoid division by zero)
        return None  # You can return None or any other value to indicate an issue

def cal_intercept(x_mean, y_mean, slope):
    return y_mean - slope * x_mean

def linear_regression(x, y):
    x_mean = cal_mean(x)
    y_mean = cal_mean(y)
    slope = cal_slope(x, y, x_mean, y_mean)

    if slope is not None:  # Check if the slope calculation was successful
        intercept = cal_intercept(x_mean, y_mean, slope)
        return slope, intercept
    else:
        return None  # Indicate that the slope could not be calculated

# Example usage:
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

result = linear_regression(x, y)
if result is not None:
    slope, intercept = result
    print("Slope:", slope)
    print("Intercept:", intercept)
else:
    print("Slope could not be calculated due to division by zero.")

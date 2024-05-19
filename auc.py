def function(x):
    return x**2

def calculate_area(a, b, n):
    delta_x = (b - a) / n
    area = 0.5 * (function(a) + function(b))  # Area of the first and last rectangles

    for i in range(1, n):
        x_i = a + i * delta_x
        area += function(x_i)

    return delta_x * area

desired_error = 0.01  # 1% error
current_error = float('inf')
n = 1

while current_error > desired_error:
    n *= 2
    current_area = calculate_area(0, 10, n)
    current_error = abs((current_area - calculate_area(0, 10, n // 2)) / current_area)

print(f"Number of subintervals (n): {n}")
print(f"Approximate area under the curve: {calculate_area(0, 10, n)}")
   
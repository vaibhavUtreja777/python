# Practical 1: Basic Python Operations and Control Structures

# Part 1: Creating variables of different data types
integer_var = 42           # Integer
float_var = 3.14          # Float
string_var = "Hello, Python!"  # String
list_var = [1, 2, 3, 4, 5]    # List

# Display variables and their types
print("Variables and their types:")
print(f"Integer: {integer_var}, Type: {type(integer_var)}")
print(f"Float: {float_var}, Type: {type(float_var)}")
print(f"String: {string_var}, Type: {type(string_var)}")
print(f"List: {list_var}, Type: {type(list_var)}")

# Part 2: Basic arithmetic operations
a = 10
b = 3
sum_result = a + b
diff_result = a - b
prod_result = a * b
div_result = a / b

print("\nArithmetic Operations:")
print(f"Sum: {a} + {b} = {sum_result}")
print(f"Difference: {a} - {b} = {diff_result}")
print(f"Product: {a} * {b} = {prod_result}")
print(f"Division: {a} / {b} = {div_result}")

# Part 3: Conditional to check if a number is positive, negative, or zero
number = float(input("\nEnter a number: "))
if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print(f"{number} is zero")

# Part 4: Loop to print first 10 Fibonacci numbers
print("\nFirst 10 Fibonacci numbers:")
n = 10
fib = [0, 1]  # Initialize with first two numbers
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])  # Next number is sum of previous two
print(fib)
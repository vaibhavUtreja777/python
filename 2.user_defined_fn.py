# Practical 2: User-Defined Functions

# Function 1: Calculate factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Function 2: Check if a string is a palindrome
def is_palindrome(text):
    # Convert to lowercase and remove spaces/punctuation
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    # Compare with its reverse
    return cleaned_text == cleaned_text[::-1]

# Part 1: Factorial calculation
try:
    num = int(input("Enter a number to calculate its factorial: "))
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(num)
        print(f"Factorial of {num} is: {result}")
except ValueError:
    print("Please enter a valid integer.")

# Part 2: Palindrome check
text = input("\nEnter a string to check if it's a palindrome: ")
if is_palindrome(text):
    print(f"'{text}' is a palindrome!")
else:
    print(f"'{text}' is not a palindrome.")
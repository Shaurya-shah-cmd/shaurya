#question 1
def math_operations(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero!"
    else:
        return "Invalid operation!"
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Choose operation: add / subtract / multiply / divide")
op = input("Enter operation: ").lower()
result = math_operations(num1, num2, op)
print(f"Result: {result}")



#question 2
def is_palindrome(number):
    original = str(number)
    reversed_num = original[::-1]
    return original == reversed_num
num = input("Enter a number to check if it's a palindrome: ")
if is_palindrome(num):
    print(f"{num} is a Palindrome Number.")
else:
    print(f"{num} is NOT a Palindrome Number.")

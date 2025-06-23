#question 1
name = input("Enter student's name: ")
student_class = input("Enter student's class: ")
print("Enter marks for 5 subjects:")
marks = []
for i in range(1, 6):
    mark = float(input(f"Subject {i} marks: "))
    marks.append(mark)
total_marks = sum(marks)
percentage = (total_marks / 500) * 100
if percentage >= 60:
    grade = 'A'
elif percentage >= 50:
    grade = 'B'
elif percentage >= 40:
    grade = 'C'
elif percentage >= 33:
    grade = 'D'
else:
    grade = 'Fail'
print("\n--- Student Result ---")
print(f"Name       : {name}")
print(f"Class      : {student_class}")
print(f"Total Marks: {total_marks}/500")
print(f"Percentage : {percentage:.2f}%")
print(f"Grade      : {grade}")


#question 2
num = int(input("Enter a number to find its factorial: "))
factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("Factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"Factorial of {num} is {factorial}")


#question 3
items = []
prices = []

while True:
    print("\n--- Billing Menu ---")
    print("1. Create Bill (Add Items)")
    print("2. Display Items with Prices and Total")
    print("3. Display Total Only")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        item_name = input("Enter item name: ")
        item_price = float(input("Enter item price: "))
        items.append(item_name)
        prices.append(item_price)
        print(f"Added {item_name} - ₹{item_price}")

    elif choice == '2':
        if not items:
            print("No items in the bill yet.")
        else:
            print("\n--- Bill Details ---")
            for i in range(len(items)):
                print(f"{items[i]} : ₹{prices[i]}")
            print(f"Total Bill Amount: ₹{sum(prices)}")

    elif choice == '3':
        print(f"Total Bill Amount: ₹{sum(prices)}")

    elif choice == '4':
        print("Exiting the billing system. Thank you!")
        break

    else:
        print("Invalid choice. Please enter 1-4.")


#question 4
numbers = [12, 45, 2, 67, 1, 90]
smallest = min(numbers)
print("Smallest number in the list is:", smallest)


#question 5
numbers = [12, 45, 2, 67, 1, 90]
unique_numbers = list(set(numbers))
unique_numbers.sort()
second_greatest = unique_numbers[-2]
print("Second greatest number is:", second_greatest)


#question 6
numbers = [12, 45, 2, 67, 1, 90]
unique_numbers = list(set(numbers))
unique_numbers.sort()
second_smallest = unique_numbers[1]
print("Second smallest number is:", second_smallest)


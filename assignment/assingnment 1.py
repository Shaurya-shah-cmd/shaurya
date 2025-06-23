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
print("\n--- Student Result ---")
print(f"Name       : {name}")
print(f"Class      : {student_class}")
print(f"Percentage : {percentage:.2f}%")


# Input two strings(question 2)
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
combined = str1 + str2
print("\n--- Combined String ---")
print("Combined:", combined)
print("\n--- String Methods Output ---")
print("Uppercase       :", combined.upper())
print("Lowercase       :", combined.lower())
print("Title Case      :", combined.title())
print("Is Alphanumeric :", combined.isalnum())
print("Length          :", len(combined))
print("First 5 chars   :", combined[:5])
print("Replace 'a' with '@' :", combined.replace('a', '@'))



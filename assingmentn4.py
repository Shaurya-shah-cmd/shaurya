import csv
import sqlite3
import pandas as pd

address_book = [
    ["Name", "Address", "Mobile", "Email"],
    ["John Doe", "123 Main Street", "9876543210", "john@example.com"],
    ["Jane Smith", "456 Maple Avenue", "9123456780", "jane@example.com"],
    ["Bob Johnson", "789 Oak Drive", "9988776655", "bob@example.com"]
]

with open("address_book.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(address_book)

print("✅ Address Book CSV created!")

weather_data = [
    ["City", "Temperature", "Humidity", "Condition"],
    ["Delhi", 35, 45, "Sunny"],
    ["Mumbai", 30, 70, "Rainy"],
    ["Bangalore", 28, 60, "Cloudy"]
]

with open("weather_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(weather_data)

# Read and display weather data
df_weather = pd.read_csv("weather_data.csv")
print("\n🌦️ Weather Data:")
print(df_weather)

# --- 3. Practice DATABASE Operations ---
# Create or connect to SQLite database
conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

# Create tables
cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
cursor.execute("CREATE TABLE IF NOT EXISTS courses (id INTEGER PRIMARY KEY, course_name TEXT, credits INTEGER)")

# Insert data into tables
cursor.execute("INSERT INTO students (name, age) VALUES ('Alice', 20)")
cursor.execute("INSERT INTO students (name, age) VALUES ('Bob', 22)")
cursor.execute("INSERT INTO courses (course_name, credits) VALUES ('Math', 4)")
cursor.execute("INSERT INTO courses (course_name, credits) VALUES ('Science', 3)")

conn.commit()

# SELECT operation
print("\n🎓 Students:")
for row in cursor.execute("SELECT * FROM students"):
    print(row)

print("\n📚 Courses:")
for row in cursor.execute("SELECT * FROM courses"):
    print(row)

# UPDATE a student's age
cursor.execute("UPDATE students SET age = 21 WHERE name = 'Alice'")
conn.commit()

# DELETE a course
cursor.execute("DELETE FROM courses WHERE course_name = 'Science'")
conn.commit()

# Show updated data
print("\n🔁 Updated Students Table:")
for row in cursor.execute("SELECT * FROM students"):
    print(row)

print("\n❌ Courses Table after Deletion:")
for row in cursor.execute("SELECT * FROM courses"):
    print(row)

# Close connection
conn.close()

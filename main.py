import csv

address_book = [
    ["Name", "Address", "Mobile", "Email"],
    ["Alice Green", "101 Park Ave", "9876543210", "alice@example.com"],
    ["Bob White", "202 Lake View", "9123456780", "bob@example.com"],
    ["Charlie Blue", "303 Ocean Drive", "9988776655", "charlie@example.com"]
]

with open("address_book.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(address_book)

print("Address Book CSV created!")

with open("address_book.csv", "r", newline="") as file:
    read = csv.reader(file)
    for i in read:
        print(i)

import requests


def get_weather(city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=b4134b1fb6c692a1791f98b7ff7aa5b0"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

    if data.get("cod") != 200:
        print(f"Error: {data.get('message')}")
        return None

    print(f"City: {data['name']}")
    print(f"Temperature: {(data['main']['temp'] - 273.15):.2f}C")
    print(f"Weather: {data['weather'][0]['description']}")
    print(f'Wind Speed :{data["wind"]["speed"] * 3.6} km/h')


city = input("Enter city name: ")
get_weather(city)
print("Weather data fetched successfully.")


# Display weather data
df_weather = pd.read_csv("weather_data.csv")
print("\n🌤️ Weather Data:")
print(df_weather)

# --- 3. SQLite Database Practice ---
# Connect or create database
conn = sqlite3.connect("practice.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
    CREATE TABLE  students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        email TEXT
    )
""")

cursor.execute("""
    CREATE TABLE courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name TEXT,
        instructor TEXT
    )
""")

cursor.execute("""
    CREATE TABLE enrollments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        course_id INTEGER,
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (course_id) REFERENCES courses(id)
    )
""")

# Insert records
cursor.executemany("INSERT INTO students (name, age, email) VALUES ", [
    ("Alice Green", 20, "alice@example.com"),
    ("Bob White", 22, "bob@example.com")
])

cursor.executemany("INSERT INTO courses (course_name, instructor) VALUES ", [
    ("Mathematics", "Dr. Rao"),
    ("Science", "Dr. Menon")
])

cursor.executemany("INSERT INTO enrollments (student_id, course_id) VALUES ", [
    (1, 1),
    (2, 2)
])

conn.commit()

# SELECT queries
print("\n Students Table:")
for row in cursor.execute("SELECT * FROM students"):
    print(row)

print("\n Courses Table:")
for row in cursor.execute("SELECT * FROM courses"):
    print(row)

print("\n Enrollments Table (with JOIN):")
for row in cursor.execute("""
    SELECT s.name, c.course_name
    FROM enrollments e
    JOIN students s ON e.student_id = s.id
    JOIN courses c ON e.course_id = c.id
"""):
    print(row)

# UPDATE operation
cursor.execute("UPDATE students SET age = 21 WHERE name = 'Alice Green'")
conn.commit()

# DELETE operation
cursor.execute("DELETE FROM courses WHERE course_name = 'Science'")
conn.commit()

# Display updated data
print("\n Updated Students Table:")
for row in cursor.execute("SELECT * FROM students"):
    print(row)

print("\n Courses Table after Deletion:")
for row in cursor.execute("SELECT * FROM courses"):
    print(row)

# Close DB
conn.close()

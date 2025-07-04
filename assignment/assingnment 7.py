#question 1
import re

email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

emails = ['test@example.com', 'invalid-email@', 'abc@xyz.org']
for e in emails:
    if re.match(email_pattern, e):
        print(e, 'is valid')
    else:
        print(e, 'is invalid')
mobile_pattern = r'^(?:\+91|0)?[6-9]\d{9}$'

numbers = ['9876543210', '+919876543210', '09876543210', '123456']
for n in numbers:
    if re.match(mobile_pattern, n):
        print(n, 'is valid')
    else:
        print(n, 'is invalid')
string_pattern = r'^[A-Za-z]+$'

words = ['HelloWorld', 'hello123', 'Test']
for w in words:
    if re.match(string_pattern, w):
        print(w, 'is valid')
    else:
        print(w, 'is invalid')
text = "My order numbers are 12345, 67890 and 11223."
numbers = re.findall(r'\d+', text)
print(numbers)
password_pattern = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'

pwds = ['pass1234', '12345678', 'abcdefg', 'GoodPass1']
for pwd in pwds:
    if re.match(password_pattern, pwd):
        print(pwd, 'is valid')
    else:
        print(pwd, 'is invalid')


# question 2
        import pandas as pd
        data = {'dates': ['2024-05-01', '2024-06-15', '2024-12-31']}
        df = pd.DataFrame(data)
        df['dates'] = pd.to_datetime(df['dates'])
        df['year'] = df['dates'].dt.year
        df['month'] = df['dates'].dt.month
        df['day'] = df['dates'].dt.d
        df['weekday'] = df['dates'].dt.day_name()
        df['plus_7_days'] = df['dates'] + pd.Timedelta(days=7)
        print(df)

 # question 3
import pandas as pd
df = pd.read_csv('your_file.csv')
print(df.head())
print(df.info())
df_cleaned = df.dropna()
df_filled = df.fillna(0)
df_cleaned = df_cleaned.drop_duplicates()
df_cleaned['SomeNumericCol'] = pd.to_numeric(df_cleaned['SomeNumericCol'], errors='coerce')
print(df_cleaned.describe())
result = df_cleaned.groupby('CategoryColumn')['Sales'].sum().reset_index()
print(result)
df_cleaned.to_csv('cleaned_file.csv', index=False)



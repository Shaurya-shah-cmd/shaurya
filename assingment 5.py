#question 1
import pandas as pd
data = {'a': 10, 'b': 20, 'c': 30}
series_from_dict = pd.Series(data)
print(series_from_dict)


data = [10, 20, 30, 40]
series_from_list = pd.Series(data)
print(series_from_list)



# Using index
print(series_from_list[0])   # First element
print(series_from_dict['b']) # Access using key

# Using slicing
print(series_from_list[1:3]) # Slice elements


#question 2

data = [[1, 'Alice'], [2, 'Bob'], [3, 'Charlie']]
df_from_2d_list = pd.DataFrame(data, columns=['ID', 'Name'])
print(df_from_2d_list)





data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df_from_dict = pd.DataFrame(data)
print(df_from_dict)




data = [['Tom', 10], ['Jerry', 15]]
df_list_of_lists = pd.DataFrame(data, columns=['Name', 'Age'])
print(df_list_of_lists)





data = [('Tom', 10), ('Jerry', 15)]
df_list_of_tuples = pd.DataFrame(data, columns=['Name', 'Age'])
print(df_list_of_tuples)



data = [{'Name': 'Tom', 'Age': 10}, {'Name': 'Jerry', 'Age': 15}]
df_list_of_dicts = pd.DataFrame(data)
print(df_list_of_dicts)



#question 3
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
})

# Method 1: Using iterrows()
for index, row in df.iterrows():
    print(index, row['Name'], row['Age'])

# Method 2: Using itertuples()
for row in df.itertuples(index=True, name='Person'):
    print(row.Index, row.Name, row.Age)


# Select rows where Age > 28
filtered_df = df[df['Age'] > 28]
print(filtered_df)



# Select the second row (index 1)
second_row = df.iloc[1]
print(second_row)




# Select first 2 rows with only 'Name' column
subset_df = df.loc[:1, ['Name']]
print(subset_df)




# Drop rows where Age is less than 30
df_dropped = df[df['Age'] >= 30]
print(df_dropped)




# New row to insert
new_row = pd.DataFrame([{'Name': 'David', 'Age': 28}])

# Insert at index 1
df_updated = pd.concat([df.iloc[:1], new_row, df.iloc[1:]]).reset_index(drop=True)
print(df_updated)




# Convert all rows to list of lists
list_of_rows = df.values.tolist()
print(list_of_rows)

# Convert each row to dictionary and form a list
list_of_dicts = df.to_dict(orient='records')
print(list_of_dicts)

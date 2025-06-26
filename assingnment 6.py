#question 1
import pandas as pd
date_strings = pd.Series(['2024-01-01', '2024-02-01', '2024-03-01'])
datetime_series = pd.to_datetime(date_strings)
time_series = pd.Series([100, 200, 300], index=datetime_series)
print(time_series)

#question 2
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David']
})
df2 = pd.DataFrame({
    'ID': [3, 4, 5, 6],
    'Score': [85, 90, 75, 88]
})
inner_merged = pd.merge(df1, df2, on='ID', how='inner')
print("Inner Merge:\n", inner_merged)
left_joined = pd.merge(df1, df2, on='ID', how='left')
print("Left Join:\n", left_joined)
right_joined = pd.merge(df1, df2, on='ID', how='right')
print("Right Join:\n", right_joined)
df1_indexed = df1.set_index('ID')
df2_indexed = df2.set_index('ID')
index_joined = df1_indexed.join(df2_indexed, how='inner')
print("Index-based Join:\n", index_joined)

#question 3
import pandas as pd
df1 = pd.DataFrame({
    'ID': [1, 2],
    'Name': ['Alice', 'Bob']
})
df2 = pd.DataFrame({
    'ID': [3, 4],
    'Name': ['Charlie', 'David']
})
df3 = pd.DataFrame({
    'ID': [2, 3, 4],
    'Score': [88, 92, 79]
})
concat_df = pd.concat([df1, df2], ignore_index=True)
print("Concatenated DataFrame:\n", concat_df)
merged_df = pd.merge(concat_df, df3, on='ID', how='inner')
print("Merged DataFrame:\n", merged_df)
df3_indexed = df3.set_index('ID')
concat_indexed = concat_df.set_index('ID')
joined_df = concat_indexed.join(df3_indexed, how='inner')
print("Join Result:\n", joined_df)

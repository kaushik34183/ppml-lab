import pandas as pd
import numpy as np

print("=== 1. Creating DataFrames ===")
# From dictionary
data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'London', 'Paris', 'Tokyo']
}
df_dict = pd.DataFrame(data_dict)
print("DataFrame from dict:")
print(df_dict)
print()

# From list of lists
data_list = [
    ['Eve', 22, 'Berlin'],
    ['Frank', 40, 'Sydney']
]
df_list = pd.DataFrame(data_list, columns=['Name', 'Age', 'City'])
print("DataFrame from list of lists:")
print(df_list)
print()

# From numpy array
arr = np.array([[45, 'Rome'], [32, 'Madrid']])
df_arr = pd.DataFrame(arr, columns=['Age', 'City'])
print("DataFrame from numpy array:")
print(df_arr)
print()

print("=== 2. Basic Info ===")
df = pd.concat([df_dict, df_list, df_arr], ignore_index=True)
print("Combined DF:")
print(df)
print("\nHead:")
print(df.head())
print("\nDescribe:")
print(df.describe())
print("\nInfo:")
print(df.info())
print()

print("=== 3. Manipulation: Add/Drop/Rename ===")
# Add column
df['Salary'] = [50000, 60000, 70000, 55000, 45000, 80000, 65000]
print("After adding Salary column:")
print(df[['Name', 'Salary']])
print()

# Drop row/column
df_dropped = df.drop(0).drop('City', axis=1)
print("After dropping row 0 and City column:")
print(df_dropped)
print()

# Rename
df_renamed = df.rename(columns={'Age': 'Years'})
print("After renaming Age to Years:")
print(df_renamed[['Name', 'Years']])
print()

print("=== 4. Selection/Indexing ===")
print("iloc[1:3]:")
print(df.iloc[1:3])
print("\nloc (Age > 30):")
print(df.loc[df['Age'] > 30])
print("\nName column:")
print(df['Name'])
print()

print("=== 5. Filtering and Sorting ===")
high_salary = df[df['Salary'] > 60000]
print("Salary > 60000:")
print(high_salary)
print()

sorted_df = df.sort_values('Age', ascending=False)
print("Sorted by Age descending:")
print(sorted_df)
print()

print("=== 6. Grouping and Aggregation ===")
grouped = df.groupby('City')['Salary'].agg(['mean', 'max'])
print("Group by City, Salary stats:")
print(grouped)
print()

print("=== 7. Apply custom function ===")
df['Age_Group'] = df['Age'].apply(lambda x: 'Young' if x < 30 else 'Senior')
print("Added Age_Group column:")
print(df[['Name', 'Age', 'Age_Group']])
print()

print("=== 8. Save and Load ===")
df.to_csv('sample_dataframe.csv', index=False)
print("Saved to CSV.")

loaded_df = pd.read_csv('sample_dataframe.csv')
print("Loaded from CSV:")
print(loaded_df.head())
print("\nTask complete: DataFrame created and manipulated successfully.")

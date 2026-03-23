import pandas as pd
data = [10, 20, 30]
labels = ['a', 'b', 'c']
series = pd.Series(data, index=labels)
print("Fixed Pandas Series:")
print(series)
print("Value at label 'b':", series['b'])

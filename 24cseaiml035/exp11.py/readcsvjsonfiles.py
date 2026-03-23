import pandas as pd
df_csv=pd.read_csv("sample.csv")
print(df_csv)
df_json=pd.read_json('sample.json')
print("\n dataframe from json:\n",df_json)
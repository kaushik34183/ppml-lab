import pandas as pd
data={
    'math':[90,85,80,90],
    'science':[88,82,85,90],
    'english':[78,75,80,85]
}
df=pd.DataFrame(data)
print("DataFrame:\n", df)
correlation=df.corr()
print("\nCorrelation matrix:\n", correlation)
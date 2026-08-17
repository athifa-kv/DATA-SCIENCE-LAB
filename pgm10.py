import pandas as pd
data={
    "Name":['Anu','Ammu','Riya','Meera','Athira'],'Age':[20,21,19,22,20],'Mark':[85,90,78,88,95]
}
df=pd.DataFrame(data)
print("Data Frame:")
print(df)
print("\nSummary Statistics:")
print(df.describe())
print("\nBasic Information:")
print(df.info())
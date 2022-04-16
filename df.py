# dataframe pandas

import pandas as pd
import numpy

print("Start")


data = { "c": [1,2,3,4,4], "d": [55,66,77,4,4], "e": [89,9,0,4,4]}
df = pd.DataFrame(data)
print("===========================")
print("===========================")
print(df)
print(df.loc[2])
print(df.loc[[0,2]])

print("===========================")
print("===========================")
df = pd.DataFrame(data, index = ["a1","a2","a3","a4","a5"])

print(df)
print("--------------")
print(df.loc["a2"])

                                                                            
print("===========================")
print("===========================")

print(df.info())
print(df.to_string())
print(df.head(2))
print(df.tail(2))

print(df["c"].max())

print(df.duplicated())
print(df.drop_duplicates(inplace=False))
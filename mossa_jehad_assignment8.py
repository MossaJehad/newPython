import pandas as pd

df = pd.read_csv("train.csv")

print(df.head())

print(df.tail(2))

print(df.shape)

print(df.columns)

df.info()


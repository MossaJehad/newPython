import pandas as pd

df = pd.read_csv("train.csv")

inclusive_select = df.loc[10 : 20]
exclusive_select = df.iloc[10 : 21] # 21 to make sure that it included in the range we select

print("Inclusive Select: \n", inclusive_select, "\n")
print("Execlusive Select \n", exclusive_select, "\n")

spec_feat = df.loc[5 : 15, ['Name', 'Sex', 'Age']]

print("Specific Features: \n", spec_feat, "\n")

spec_iloc = df.iloc[50 : 101, 2 : 10]

print("Specific Features with iloc: \n", spec_iloc, "\n")

name_and_age = df.loc[:, 'Name' : 'Age']

print("Name and Age for all passengers \n", name_and_age, "\n")

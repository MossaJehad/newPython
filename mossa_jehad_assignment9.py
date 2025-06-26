import pandas as pd 
 
df = pd.read_csv("train.csv") 
 
cleaned = df.dropna().drop_duplicates() 
 
first_class_pass = cleaned[cleaned['Pclass'] == 1] 
 
under_age = cleaned[cleaned["Age"] < 18] 
 
survived = cleaned[cleaned["Survived"] == 1]["Name"] 
 
pass_count_each_class = cleaned.groupby("Pclass").count() 
 
avg_age = cleaned["Age"].mean() 
 
exp_ticket = cleaned[cleaned["Fare"] > 100] 
 
print(df)
print(cleaned)
print(first_class_pass)
print(under_age)
print(survived)
print(pass_count_each_class)
print(avg_age)
print(exp_ticket)

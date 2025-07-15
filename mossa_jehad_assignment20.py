import pandas as pd

df = pd.read_csv("train.csv")
print(df.isnull().sum())

df = df.drop_duplicates()

Age = df['Age'].mean() # avg age (bcz it's logical duh)

df['Age'] = df['Age'].fillna(Age)

df['Cabin'] = df['Cabin'].fillna('-')

import re

def cabin_to_number(cabin):
	if cabin == '-' or pd.isna(cabin):
		return 0

	match = re.match(r"([A-Za-z])(\d+)", cabin)
	if not match:
		return 0

	letter, number = match.groups()
	number = int(number)
	letter = letter.upper()

	multiplier_map = {'A': 0, 'B': 150, 'C': 300}

	return number + multiplier_map.get(letter, 0)


df['Cabin'] = df['Cabin'].apply(cabin_to_number)

print(df['Cabin'])

Embarked = df['Embarked'].mode()[0] # most frequent (2 values only)

df['Embarked'] = df['Embarked'].fillna(Embarked)

df['Sex'] = df['Sex'].replace({'male': 1, 'female': 0})

df = pd.get_dummies(df, columns = ['Ticket'])
df = pd.get_dummies(df, columns = ['Embarked'])

print(df)

df = df.drop('Name', axis = 1)
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X = df.drop('Survived', axis = 1)
y = df['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Classification Report: \n", classification_report(y_test, y_pred))

print(f"Accuracy Score: %{accuracy_score(y_test, y_pred) * 100:.4f}")

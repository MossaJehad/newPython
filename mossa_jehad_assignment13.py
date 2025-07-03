import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder 


df = pd.read_csv("Iris.csv")

df["Species"] = df["Species"].replace("Iris-setosa", 0)
df["Species"] = df["Species"].replace("Iris-versicolor", 1)
df["Species"] = df["Species"].replace("Iris-virginica", 2)

df.isna().sum()

X_tr, X_ts, Y_tr, Y_ts = train_test_split(df.drop("Species", axis=1), df["Species"], test_size=0.2, random_state=42)

model = SVC(kernel="linear", C=75)
model.fit(X_tr, Y_tr)

print(classification_report(Y_ts, model.predict(X_ts)))



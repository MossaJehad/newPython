import gradio as gr
import pandas as pd
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.svm import SVC

df = pd.read_csv("Student_Performance.csv")
df_clean = df.drop_duplicates()
df_clean.loc[:, "Extracurricular Activities"] = df_clean["Extracurricular Activities"].map({'Yes': 1, 'No': 0})
df_clean.head()

X = df_clean.iloc[:, :-1].values
y = np.squeeze(df_clean.iloc[:, 5:6].values)

X_tr, X_ts, y_tr, y_ts = train_test_split(X, y, test_size=0.2, random_state=42)

model = SVC(kernel="linear", C=75)
model.fit(X_tr, y_tr)

def pred(a, b, c, d, e):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        e = int(e)
    except:
        return "You entered non-numerical value"
    if(a < 0 or b < 0 or d < 0 or e < 0):
        return "Please enter positive numbers"
    if(c > 1 or c < 0):
        return "Please enter only 1 or 0 for the Extra Activities"
    pred = model.predict([[a, b, c, d, e]])
    try:
        pred = int(pred)
    except:
        return "Something went wrong!"
    if(pred <= 0 or not pred):
        return "0"
    else:
        return pred

StudyH = gr.Number(label = "Hours Studied")
PrevSc = gr.Number(label = "Previous Scores")
ExtraA = gr.Number(label = "Extra Activities Yes=1, No=0")
SleepH = gr.Number(label = "Sleep Hours")
PPract = gr.Number(label = "Sample Question Papers Practiced")

demo = gr.Interface(
        fn = pred,
        inputs = [StudyH, PrevSc, ExtraA, SleepH, PPract],
        outputs = "text",
        title = "Performance Predict",
)

demo.launch()

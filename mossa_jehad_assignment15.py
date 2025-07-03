import gradio as gr
import pandas as pd
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder

userInput = input(f"""What page do you want to visit:
                  Enter 1 to visit Flower Predection page
                  Enter 2 to visit Salary Predection page
                  :""")

try:
    userInput = int(userInput)
except:
    print("Please enter numbers only")
    exit()

if (userInput == 1):

    df = pd.read_csv("Iris.csv")

    df["Species"] = df["Species"].replace("Iris-setosa", 0)
    df["Species"] = df["Species"].replace("Iris-versicolor", 1)
    df["Species"] = df["Species"].replace("Iris-virginica", 2)

    df.isna().sum()

    X_tr, X_ts, Y_tr, Y_ts = train_test_split(df.drop(["Id", "Species"], axis=1), df["Species"], test_size=0.2, random_state=42)

    model = SVC(kernel="linear", C=75)
    model.fit(X_tr, Y_tr)

    def pred(a, b, c, d):
        if(0 > a or 0 > b or 0 > c or 0 > d or a > 25 or b > 25 or c > 25 or d > 25):
            return "Please enter Numbers between 0 - 25"
        spec = model.predict([[a, b, c, d]])
        if(spec == 0):
            return "Iris-setosa"
        elif(spec == 1):
            return "Iris-versicolor"
        elif(spec == 2):
            return "Iris-virginica"
        else:
            return "Unkown"

    Slength = gr.Number(label="SepalLengthCm")
    SWidth = gr.Number(label="SepalWidthCm")
    PLength = gr.Number(label="PetalLengthCm")
    PWidth = gr.Number(label="PetalWidthCm")

    demo1 = gr.Interface(
        fn = pred,
        inputs = [Slength, SWidth, PLength, PWidth],
        outputs = "text",
        title = "Flowers",
    )

    demo1.launch()

elif(userInput == 2):
    df = pd.read_csv("salary_data.csv")

    X = df["YearsExperience"]
    Y = df["Salary"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)

    X_rain_reshaped = X_train.values.reshape(-1, 1)

    model = LinearRegression()
    model.fit(X_rain_reshaped, Y_train)

    def pred(x):
        if(0 > x or x > 25):
            return "Please enter numbers between 0 and 25"
        return int(model.predict([[x]]))

    inputf = gr.Number(label="YOE")

    demo = gr.Interface(
        fn = pred,
        inputs = inputf,
        outputs = "text",
        title = "Salary Expectation",
    )

    demo.launch()

else:
    print("Please enter either 1 or 2 only!")
    exit()

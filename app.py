from flask import Flask, render_template, request
import pickle
import numpy as np

import warnings
from sklearn.exceptions import InconsistentVersionWarning
warnings.filterwarnings("ignore", category=InconsistentVersionWarning)

app = Flask(__name__)
 
model = pickle.load(open(r'C:\Users\pc\Desktop\KNN Algorithm for Boston Data Set_Regression\expense_model.pkl', 'rb'))

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            CRIM = float(request.form["CRIM"])
            ZN = float(request.form["ZN"])
            INDUS = float(request.form["INDUS"])
            CHAS = float(request.form["CHAS"])
            NOX = float(request.form["NOX"])
            RM = float(request.form["RM"])
            AGE = float(request.form["AGE"])
            DIS = float(request.form["DIS"])
            RAD = float(request.form["RAD"])
            TAX = float(request.form["TAX"])
            PTRATIO = float(request.form["PTRATIO"])
            B = float(request.form["B"])
            LSTAT = float(request.form["LSTAT"])
            
            input_data = np.array([[CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT]])
            prediction = model.predict(input_data)[0]
            return render_template("index.html", prediction_text='Predicted House Price: ${:.2f}'.format(prediction))
        except ValueError:
            return render_template("index.html", prediction_text="Invalid input. Please enter valid numbers.")

if __name__ == "__main":
    app.run()

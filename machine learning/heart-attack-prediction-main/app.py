import flask
from flask import Flask , request, render_template
import numpy as np
import pickle




app = Flask(__name__)
stored_data = pickle.load(open("heartAttack.sav","rb"))

@app.route("/", methods = ["GET"])
def home():
    return render_template("heart.html")



@app.route("/diagnosis" , methods = ["POST"])
def prediction():
    user_name = request.form["name"]
    Age = int(request.form["Age"])
    cp = int(request.form["cp"])
    gender = int(request.form["gender"])
    trestbps = int(request.form["trestbps"])
    chol = int(request.form["chol"])
    fbs = int(request.form["fbs"])
    restecg = int(request.form["restecg"])
    thalach = int(request.form["thalach"])
    slope = int(request.form["slope"])

    prediction = stored_data.predict([[Age, cp, gender, trestbps, chol, fbs, restecg, thalach, slope]])[0]
    if prediction == 0:
       prediction= "no chances of heart attack"
    else:
        prediction = "chances of heart attack"
    return render_template("heart.html", prediction = prediction)


    




if __name__ == "__main__":
    app.run(debug=True)


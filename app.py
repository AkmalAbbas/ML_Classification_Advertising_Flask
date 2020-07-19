from flask import Flask, render_template , redirect , request , flash
from forms import AdvertisingForm
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

app= Flask(__name__)
app.secret_key = "advertising"
advetising_model = pickle.load(open('model.pkl','rb'))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/c-model-advertising",methods=["POST","GET"])
def c_model_advertising():
    result = None
    form = AdvertisingForm(request.form)
    if form.validate() == False:
        flash('All fields are required.')
    else:
        time_spend = request.form["time_spend"]
        age = request.form["age"]
        area_income = request.form["area_income"]
        internet_usage = request.form["internet_usage"]
        gender = request.form["gender"]
        print(time_spend)
        input_features = [[float(time_spend),int(age),float(area_income),float(internet_usage),int(gender)]]
        print(input_features)
        out = advetising_model.predict(input_features)
        if out == 0:
            result = "will not clicked"
        else:
            result = "will click"

    return render_template('AdvertisingModel.html',result = f"The user {result} the ad !!!!" , form = form)


if __name__ == "__main__":
    app.run()

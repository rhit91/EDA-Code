from flask import Flask,request , jsonify, render_template
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

##import ridge regressor model and standard scaler model
ridge_model = pickle.load(open('models/ridge.pkl' , 'rb')) 
standar_scaler = pickle.load(open('models/scaler.pkl' , 'rb'))

#3 Route for home page
@app.route('/')
def index():
    return render_template('index.html')



@app.route('/predictdata' , methods= ['GET' , 'POST'])
def predict_datapoint():
    if request.method == 'POST':
         Temprature = float(request.form.get('Temprature'))
         RH = float(request.form.get('RH'))
         WS = float(request.form.get('WS'))
         Rain = float(request.form.get('Rain'))
         FFMC = float(request.form.get('FFMC'))
         DMC = float(request.form.get('DMC'))
         ISI = float(request.form.get('ISI'))
         Classes = float(request.form.get('Classes'))
         Region = float(request.form.get('Region'))



         ## Make Sure Above order is Correct, so that model trained can predict perfectly#



         new_data_scaled = standard_scaler.transform([[Temprature , RH, WS, Rain, FFMC, DMC, ISI, Classes, Region ]])
         result = ridge_model.predict(new_data_scaled)

         return render_template('home.html' , result= result[0])
    else:
        return render_template('home.html')


if __name__=="__main__":
    app.run(host="0.0.0.0")

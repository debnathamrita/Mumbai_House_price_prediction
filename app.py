import pandas as pd
import numpy as np
from flask import Flask, render_template, request
import joblib
from sklearn.ensemble import RandomForestRegressor


# Load model and feature names
model = joblib.load('model_filename.joblib')
feature_names = joblib.load('feature_names.joblib')

# Create a DataFrame from user input
user_data = pd.DataFrame(columns=feature_names)

#Load the category lists
status_list = joblib.load('status_list.joblib')
age_list =  joblib.load('age_list.joblib')
type_list = joblib.load('type_list.joblib')
locality_list = joblib.load('locality_list.joblib')
region_list = joblib.load('region_list.joblib')




# Flask app
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    prediction = None
    if request.method == "POST":
        # Input from user
        user_data = pd.DataFrame(columns=feature_names)
        # initialize all to zero
        user_data.loc[0] = 0  
        
        user_data.loc[0, 'bhk'] = float(request.form['bhk'])
        user_data.loc[0, 'area'] = float(request.form['area'])
        
        # Type dummies
        for t in type_list[:]:
            user_data.loc[0, f'type_{t}'] = 1 if t == request.form['type'] else 0
        
        # Status dummies 
        for s in status_list[:]:
            user_data.loc[0, f'status_{s}'] = 1 if s == request.form['status'] else 0
        
        # Age dummies
        for a in age_list[:]:
            user_data.loc[0, f'age_{a}'] = 1 if a == request.form['age'] else 0
        
        # Locality dummies
        for l in locality_list[:]:
            user_data.loc[0, f'locality_simplified_{l}'] = 1 if l == request.form['locality'] else 0
        
        # Region dummies
        for r in region_list[:]:
            user_data.loc[0, f'region_simplified_{r}'] = 1 if r == request.form['region'] else 0
        
        # Predict
        price = model.predict(user_data)[0]
        prediction = round(price, 2)
    return render_template('form.html', 
                         prediction=prediction, 
                         locality_list=locality_list, 
                         region_list=region_list,
                         type_list=type_list,
                         status_list=status_list,
                         age_list=age_list)

if __name__ == '__main__':
    app.run(debug=True) 
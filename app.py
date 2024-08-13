from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

dtr = pickle.load(open('indu.pkl', 'rb'))
preprocessor = pickle.load(open('preprocessor.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    Year = request.form['Year']
    average_rain_fall_mm_per_year = request.form['average_rain_fall_mm_per_year']
    pesticides_tonnes = request.form['pesticides_tonnes']
    avg_temp = request.form['avg_temp']
    Area = request.form['Area']
    Item = request.form['Item']

    features = np.array([[Year, average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp, Area, Item]], dtype=object)
    transformed_features = preprocessor.transform(features)
    prediction = dtr.predict(transformed_features)[0]

    return render_template('result.html', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# load the model
load_model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html', **locals())

@app.route('/predict', methods = ['POST', 'GET'])
def predict():
    hemoglobin = float(request.form['hemoglobin'])
    age_of_mother = float(request.form['age_of_mother'])
    age_father = float(request.form['age_father'])
    weight_before_preg = float(request.form['weight_before_preg'])
    height = float(request.form['height'])
    bmi = float(request.form['bmi'])
    yrs_of_marriage = float(request.form['yrs_of_marriage'])
    gastric_preg = float(request.form['gastric_preg'])
    education = float(request.form['education'])
    nbirths= float(request.form['nbirths'])

    prediction = load_model.predict([[hemoglobin, age_of_mother, age_father, weight_before_preg, height, bmi, yrs_of_marriage, gastric_preg, education, nbirths]])[0]
    return render_template('index.html', **locals())
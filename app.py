from flask import Flask, render_template, request
import pickle
import numpy as np
import DBModule

app = Flask(__name__)
db = DBModule.DBModule()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/input')
def input():
    return render_template('input.html')

@app.route('/wine_info')
def wine_info():
    return render_template('wine_info.html')

@app.route('/result')
def result():
    with open('model.pkl', 'rb') as file: 
        model = pickle.load(file)
    
    country = request.form['country']
    designation = request.form['designation']
    price = request.form['price']
    province = request.form['province']
    region_1 = request.form['region_1']
    region_2 = request.form['region_2']
    variety = request.form['variety']
    winery = request.form['winery']
    
    pred = model.predict([[country, designation, float(price), province, region_1, region_2, variety, winery]])
    return render_template('result.html', data=pred)

@app.route('/more_wine')
def more_wine():
    return render_template('more_wine.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    

# Insurance Cost Prediction Web App

This project predicts medical insurance costs using Machine Learning and Flask.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20App-black)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Model-green)
![Deployment](https://img.shields.io/badge/Deployment-Render-purple)

## Technologies Used
- Python
- Scikit-Learn
- XGBoost
- Flask
- HTML

## Features
- User inputs health data
- Machine learning model predicts insurance charges
- Web interface using Flask

## Input Features
- Age
- Sex
- BMI
- Children
- Smoker
- Region

## Model
XGBoost Regressor with R² score ≈ 0.86

## Project Overview

This project predicts medical insurance costs based on user attributes such as age, BMI, smoking status, region, and number of children.

The application uses a trained machine learning model and provides predictions through a Flask-based web interface.

Users can enter their information in the web form and instantly receive an estimated insurance cost.


## How to Run

1. Install dependencies

pip install -r requirements.txt

2. Run the app

python app.py

3. Open browser

http://127.0.0.1:5000

## Live Demo

https://insurance-cost-prediction-03c8.onrender.com

## Application Preview

![App screenshot](Screenshot.png)
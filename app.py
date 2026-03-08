from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# load model and scaler
model = pickle.load(open("model/insurance_model.pkl", "rb"))
scaler = pickle.load(open("model/scaler.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    age = float(request.form["age"])
    sex = int(request.form["sex"])
    bmi = float(request.form["bmi"])
    children = int(request.form["children"])
    smoker = int(request.form["smoker"])
    region = request.form["region"]

    # initialize region variables
    northwest = 0
    southeast = 0
    southwest = 0

    if region == "northwest":
        northwest = 1
    elif region == "southeast":
        southeast = 1
    elif region == "southwest":
        southwest = 1

    # scale age and bmi
    scaled = scaler.transform([[age, bmi]])
    age_scaled = scaled[0][0]
    bmi_scaled = scaled[0][1]

    # prepare model input
    features = np.array([[age_scaled, sex, bmi_scaled, children, smoker,
                          northwest, southeast, southwest]])

    # prediction
    prediction = model.predict(features)

    return render_template(
        "index.html",
        prediction_text=f"Estimated Insurance Cost: ${prediction[0]:.2f}"
    )


if __name__ == "__main__":
    app.run(debug=True)
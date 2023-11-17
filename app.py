from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained Random Forest Classifier
model = joblib.load("Liver1.pkl")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/form")
def prediction_form():
    return render_template("form.html")

@app.route("/facts")
def facts():
    return render_template("facts.html")

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        # Get user inputs from the form
        
        # Extract and convert additional features
        input_data={
            'age' : int(request.form["age"]),
            'gender' : int(request.form["gender"]),
            'total_bilirubin' : float(request.form["total_Bilirubin"]),
            'direct_bilirubin' : float(request.form["direct_Bilirubin"]),
            'alkaline_phosphatase' : int(request.form["alkaline_Phosphotase"]),
            'alanine_aminotransferase' : int(request.form["alamine_Aminotransferase"]),
            'aspartate_aminotransferase' : int(request.form["aspartate_Aminotransferase"]),
            'total_proteins' : float(request.form["total_Proteins"]),
            'albumin' : float(request.form["albumin"]),
            'albumin_and_globulin_ratio' : float(request.form["albumin_Globulin_Ratio"])
        }
        input_list=[list(input_data.values())]
       

        # Combine all features into a single list
        
        # Make prediction using the loaded model
        prediction = model.predict(input_list)

        # Display the prediction on the result page
        if prediction == 1:
            result="  LIVER DISEASE"
        else:
            result= "  NO LIVER DISEASE"
        return render_template("result.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)

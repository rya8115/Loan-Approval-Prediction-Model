from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("loan_approval_predictionn.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    no_of_dependents = int(request.form["no_of_dependents"])
    self_employed = int(request.form["self_employed"])
    income_annum = float(request.form["income_annum"])
    loan_amount = float(request.form["loan_amount"])
    loan_term = float(request.form["loan_term"])
    cibil_score = float(request.form["cibil_score"])
    residential_assets_value = float(request.form["residential_assets_value"])
    commercial_assets_value = float(request.form["commercial_assets_value"])
    luxury_assets_value = float(request.form["luxury_assets_value"])
    bank_asset_value = float(request.form["bank_asset_value"])
    education_graduate = int(request.form["education_graduate"])
    education_not_graduate = int(request.form["education_not_graduate"])

    features = np.array([[
        no_of_dependents,
        self_employed,
        income_annum,
        loan_amount,
        loan_term,
        cibil_score,
        residential_assets_value,
        commercial_assets_value,
        luxury_assets_value,
        bank_asset_value,
        education_graduate,
        education_not_graduate
    ]])

    prediction = model.predict(features)[0]

    if prediction == 1:
        result = "Loan Approved"
    else:
        result = "Loan Rejected"

    # CIBIL rating label
    if cibil_score >= 750:
        cibil_label = "Excellent"
    elif cibil_score >= 700:
        cibil_label = "Good"
    elif cibil_score >= 650:
        cibil_label = "Fair"
    elif cibil_score >= 550:
        cibil_label = "Average"
    else:
        cibil_label = "Poor"

    # CIBIL position % for gauge (300 to 900 range)
    cibil_percent = int(((cibil_score - 300) / 600) * 100)

    # Total assets
    total_assets = residential_assets_value + commercial_assets_value + luxury_assets_value + bank_asset_value

    return render_template("index.html",
        prediction_text=result,
        income=int(income_annum),
        loan_amount=int(loan_amount),
        loan_term=int(loan_term),
        cibil_score=int(cibil_score),
        cibil_label=cibil_label,
        cibil_percent=cibil_percent,
        residential=int(residential_assets_value),
        commercial=int(commercial_assets_value),
        luxury=int(luxury_assets_value),
        bank=int(bank_asset_value),
        total_assets=int(total_assets),
        dependents=no_of_dependents,
        self_employed=self_employed,
        education="Graduate" if education_graduate == 1 else "Not Graduate"
    )

app.run(host="0.0.0.0", port=7860, debug=True)
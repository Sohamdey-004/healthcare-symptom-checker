"""
Healthcare Symptom Checker - Web Version

Author: 
Soham Dey
Srijita Patra

A Flask-based healthcare awareness application that analyzes
user-reported symptoms and provides basic guidance.
NOTE: This is NOT a medical diagnosis tool.
"""

from flask import Flask, render_template, request
from logger import log_event

app = Flask(__name__)


def analyze_symptoms(data):
    """Rule-based symptom analysis (no loops used)."""

    if data["fever"] and data["cough"] and data["breathing"] and data["taste_loss"]:
        return "Possible COVID-19", "Isolate yourself and consult a doctor immediately."

    if data["fever"] and data["headache"] and data["fatigue"]:
        return "Viral Fever", "Take rest, stay hydrated, and consult a physician."

    if data["cold"] and data["sore_throat"] and not data["fever"]:
        return "Common Cold", "Warm fluids and rest are advised."

    if data["chest_pain"] and data["breathing"]:
        return "Emergency Condition", "Seek immediate medical attention."

    if data["nausea"] and data["diarrhoea"]:
        return "Stomach Infection", "Drink ORS and consult a healthcare provider."

    return "Condition Unclear", "Please consult a healthcare professional."


@app.route("/", methods=["GET", "POST"])
def index():
    condition = None
    advice = None

    if request.method == "POST":
        symptoms = {
            "fever": request.form.get("fever") == "yes",
            "cough": request.form.get("cough") == "yes",
            "breathing": request.form.get("breathing") == "yes",
            "headache": request.form.get("headache") == "yes",
            "fatigue": request.form.get("fatigue") == "yes",
            "sore_throat": request.form.get("sore_throat") == "yes",
            "cold": request.form.get("cold") == "yes",
            "chest_pain": request.form.get("chest_pain") == "yes",
            "nausea": request.form.get("nausea") == "yes",
            "diarrhoea": request.form.get("diarrhoea") == "yes",
            "taste_loss": request.form.get("taste_loss") == "yes",
        }

        condition, advice = analyze_symptoms(symptoms)
        log_event(symptoms, condition)

    return render_template("index.html", condition=condition, advice=advice)


if __name__ == "__main__":
    app.run(debug=True)

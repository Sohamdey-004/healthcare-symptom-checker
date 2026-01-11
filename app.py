"""
Healthcare Symptom Checker - Web Version

Authors:
- Soham Dey
- Srijita Patra
- Abhradeep Adhikari

Description:
A web-based healthcare awareness system that analyzes
user-selected symptoms using rule-based logic, suggests
traditional home remedies, and provides AI-generated
health suggestions using Groq.

NOTE:
This is NOT a medical diagnosis tool.
"""

from flask import Flask, render_template, request

# --- Project Imports ---
from data import DISEASE_DATA
from logger import log_event
from ai_helper import generate_ai_explanation

app = Flask(__name__)

# -------------------------------------------------
# 🔹 DYNAMIC SYMPTOM EXTRACTION (IMPORTANT PART)
# -------------------------------------------------
# This ensures symptoms are NOT hard-coded in HTML
ALL_SYMPTOMS = sorted(
    {symptom for disease in DISEASE_DATA.values() for symptom in disease["symptoms"]}
)


def analyze_symptoms(user_symptoms):
    """
    Analyze symptoms using data-driven rules.
    Disease logic is NOT hard-coded here.
    """

    for disease, info in DISEASE_DATA.items():
        if all(user_symptoms.get(symptom) for symptom in info["symptoms"]):
            return {
                "condition": disease,
                "advice": info["advice"],
                "traditional": info["traditional"]
            }

    return {
        "condition": "Condition Unclear",
        "advice": "Please consult a healthcare professional.",
        "traditional": []
    }


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    ai_text = None

    if request.method == "POST":
        # Build symptom dictionary dynamically from form
        user_symptoms = {
            symptom: request.form.get(symptom) == "yes"
            for symptom in ALL_SYMPTOMS
        }

        # Rule-based condition detection
        result = analyze_symptoms(user_symptoms)

        # AI suggestions (runs after clicking "Check Symptoms")
        ai_text = generate_ai_explanation(
            result["condition"],
            [k for k, v in user_symptoms.items() if v]
        )

        # Log event (no personal data)
        log_event(user_symptoms, result["condition"])

    return render_template(
        "index.html",
        symptoms=ALL_SYMPTOMS,
        condition=result["condition"] if result else None,
        advice=result["advice"] if result else None,
        traditional=result["traditional"] if result else None,
        ai_explanation=ai_text
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)



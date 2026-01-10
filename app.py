"""
Healthcare Symptom Checker - Web Version

Authors:
- Soham Dey
- Srijita Patra
- Abhradeep Adhikari

Description:
Rule-based healthcare awareness system with traditional remedies
and AI-generated suggestions using Groq.
NOTE: This is NOT a medical diagnosis tool.
"""

from flask import Flask, render_template, request
from data import DISEASE_DATA
from logger import log_event
from ai_helper import generate_ai_explanation

app = Flask(__name__)


def analyze_symptoms(user_symptoms):
    """
    Data-driven symptom analysis.
    No disease logic is hard-coded.
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
        user_symptoms = {
            "fever": request.form.get("fever") == "yes",
            "cold": request.form.get("cold") == "yes",
            "cough": request.form.get("cough") == "yes",
            "sore_throat": request.form.get("sore_throat") == "yes",
            "headache": request.form.get("headache") == "yes",
            "fatigue": request.form.get("fatigue") == "yes",
            "nausea": request.form.get("nausea") == "yes",
            "diarrhoea": request.form.get("diarrhoea") == "yes",
        }

        result = analyze_symptoms(user_symptoms)

        # AI suggestion ALWAYS runs after clicking Check Symptoms
        ai_text = generate_ai_explanation(
            result["condition"],
            [k for k, v in user_symptoms.items() if v]
        )

        log_event(user_symptoms, result["condition"])

    return render_template(
        "index.html",
        condition=result["condition"] if result else None,
        advice=result["advice"] if result else None,
        traditional=result["traditional"] if result else None,
        ai_explanation=ai_text
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)




"""
data.py

Centralized data layer for the Healthcare Symptom Checker.
All diseases, symptoms, medical advice, and traditional
home remedies are defined here.

This ensures:
- No hard-coded logic in app.py
- Easy scalability
- Clean separation of concerns
"""

DISEASE_DATA = {

    "Common Cold": {
        "symptoms": [
            "cold",
            "sore_throat",
            "cough"
        ],
        "advice": (
            "Take adequate rest, stay hydrated, and consult a doctor "
            "if symptoms persist or worsen."
        ),
        "traditional": [
            "Drink warm water frequently",
            "Steam inhalation with eucalyptus oil",
            "Ginger and honey tea",
            "Avoid cold food and drinks"
        ]
    },

    "Viral Fever": {
        "symptoms": [
            "fever",
            "headache",
            "fatigue"
        ],
        "advice": (
            "Rest properly, drink plenty of fluids, and seek medical "
            "attention if fever remains high."
        ),
        "traditional": [
            "Tulsi (holy basil) tea",
            "Warm turmeric milk",
            "Light and nutritious diet",
            "Adequate sleep"
        ]
    },

    "Stomach Infection": {
        "symptoms": [
            "nausea",
            "diarrhoea",
            "fatigue"
        ],
        "advice": (
            "Maintain hydration using ORS and consult a healthcare "
            "professional if symptoms continue."
        ),
        "traditional": [
            "ORS or rice water",
            "Banana and curd",
            "Avoid oily and spicy foods",
            "Coconut water"
        ]
    },

    "Migraine / Severe Headache": {
        "symptoms": [
            "headache",
            "nausea",
            "fatigue"
        ],
        "advice": (
            "Rest in a quiet, dark environment and consult a doctor "
            "if headaches are frequent."
        ),
        "traditional": [
            "Apply cold compress on forehead",
            "Adequate sleep",
            "Limit screen exposure",
            "Hydration"
        ]
    },

    "Food Poisoning": {
        "symptoms": [
            "nausea",
            "diarrhoea",
            "fever"
        ],
        "advice": (
            "Stay hydrated and seek medical help if symptoms worsen "
            "or dehydration occurs."
        ),
        "traditional": [
            "ORS solution",
            "Boiled rice and curd",
            "Ginger tea",
            "Avoid outside food"
        ]
    }
}



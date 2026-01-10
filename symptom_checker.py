print("===================================")
print("   HEALTHCARE SYMPTOM CHECKER")
print("===================================")

print("\nAnswer with YES or NO\n")

fever = input("Do you have fever? ").lower()
cough = input("Do you have cough? ").lower()
breathing = input("Do you have difficulty in breathing? ").lower()
headache = input("Do you have headache? ").lower()
fatigue = input("Do you feel fatigue? ").lower()
sore_throat = input("Do you have sore throat? ").lower()
cold = input("Do you have cold or runny nose? ").lower()
chest_pain = input("Do you have chest pain? ").lower()
nausea = input("Do you feel nausea or vomiting? ").lower()
diarrhoea = input("Do you have diarrhoea? ").lower()
taste_loss = input("Loss of taste or smell? ").lower()

print("\n-----------------------------------")

if fever == "yes" and cough == "yes" and breathing == "yes" and taste_loss == "yes":
    print("Possible Condition: COVID-19")
    print("Advice: Isolate yourself and consult a doctor immediately.")

elif fever == "yes" and headache == "yes" and fatigue == "yes":
    print("Possible Condition: Viral Fever")
    print("Advice: Take rest, stay hydrated, and consult a physician.")

elif sore_throat == "yes" and cold == "yes" and fever == "no":
    print("Possible Condition: Common Cold")
    print("Advice: Rest, warm fluids, and steam inhalation.")

elif cough == "yes" and breathing == "yes":
    print("Possible Condition: Asthma or Respiratory Infection")
    print("Advice: Avoid dust, use prescribed inhalers, and consult a doctor.")

elif headache == "yes" and fatigue == "yes" and nausea == "yes":
    print("Possible Condition: Migraine")
    print("Advice: Rest in a dark room and avoid screen exposure.")

elif chest_pain == "yes" and breathing == "yes":
    print("Possible Condition: Possible Heart or Lung Issue")
    print("Advice: Seek emergency medical help immediately.")

elif diarrhoea == "yes" and nausea == "yes":
    print("Possible Condition: Food Poisoning or Stomach Infection")
    print("Advice: Drink ORS, stay hydrated, and consult a doctor.")

else:
    print("Condition unclear.")
    print("Advice: Please consult a healthcare professional.")

print("-----------------------------------")
print("NOTE: This is NOT a medical diagnosis.")
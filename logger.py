import datetime


def log_event(symptoms, condition):
    with open("health_log.txt", "a") as file:
        file.write(
            f"{datetime.datetime.now()} | Symptoms: {symptoms} | Result: {condition}\n"
        )

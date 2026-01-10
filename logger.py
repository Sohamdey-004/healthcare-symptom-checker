import datetime


def log_event(symptoms, result):
    """Logs symptom checks for record keeping."""

    with open("health_log.txt", "a") as file:
        file.write(
            f"{datetime.datetime.now()} | Symptoms: {symptoms} | Result: {result}\n"
        )

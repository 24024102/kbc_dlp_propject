import os
import random 
def generate_data():
    os.makedirs('emails', exist_ok=True)
    templates = [
        "Hi Team,attached is the monthly report",
        "Don't forget the pizza party on friday",
        "URGENT: My credit card is 4242-4242-4242-4242, Help me!",
        "The project details are INTERNAL ONLY and strictly private",
        "Here is my IBAN: BG12KBCB9876543210 for the refaund0,",
        "The salary ;ists is in the next folder"
    ]

    for i in range(10):
        with open(f"emails/mail_{i}.txt", "w", encoding = "utf-8") as f:
            f.write(random.choice(templates))
    print("10 mock emails generated in /emails folder")

if __name__ == "__main__":
        generate_data()
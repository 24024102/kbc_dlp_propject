import os
import random 
#def generate_data():
 #   os.makedirs('emails', exist_ok=True)
    #templates = [
   #     "Hi Team,attached is the monthly report",
   #     "Don't forget the pizza party on friday",
  #      "URGENT: My credit card is 4242-4242-4242-4242, Help me!",
    #    "The project details are INTERNAL ONLY and strictly private",
   #     "Here is my IBAN: BG12KBCB9876543210 for the refaund0,",
   #     "The salary ;ists is in the next folder"
   # ]

   # for i in range(10):
  #      with open(f"emails/mail_{i}.txt", "w", encoding = "utf-8") as f:
   #         f.write(random.choice(templates))
   # print("10 mock emails generated in /emails folder")

#if __name__ == "__main__":
 #       generate_data()

def generate_enterpise_data(count=100):
    os.makedirs('emails', exist_ok=True)

    safe = ["Metting at 10 Am", "Please review the menu", "Public press realese"]
    warning = ["My salary info is attached.", "Internal project notes.", "Private phone number."]
    critical = [
        "Crad: 4242-4242-4242-4242",
        "IBAN: BG99KBC92134212321",
        "Top Secret: Passwor is 'dmin123'"
    ]

    for i in range(count):
        with open(f"emails/mail_{i}.txt", "w", encoding= "utf-8") as f:
            chance = random.random()
            if chance < 0.7:
                text = random.choice(safe)
            elif chance < 0.9:
                text = random.choice(warning) + "" + random.choice(safe)
            else:
                text = random.choice(critical) + "" + random.choice(warning)
        print(f"Generated: {count} enterprises_grade mock emails")
if __name__ == "__main__":
    generate_enterpise_data(100)        

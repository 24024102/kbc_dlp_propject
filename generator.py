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

def generate_data(count=100):
    os.makedirs('emails', exist_ok=True)
    
   
    safe_templates = [
        "Can we reschedule the meeting to 3 PM?",
        "The weather in Varna is great today, let's have lunch outside.",
        "Please find the public documentation attached to this email.",
        "Happy birthday! Wishing you all the best.",
        "The new coffee machine has arrived in the breakroom.",
        "Has anyone seen my notebook? I left it near the printer."
    ]


    warning_templates = [
        "INTERNAL ONLY: Please review the updated employee handbook.",
        "Don't share this, but I think the bonus structure is changing.",
        "The password for the guest Wi-Fi is 'KBC_Guest_2026'.",
        "Private: My personal phone number is +359 888 123 456.",
        "The draft for Project X is strictly for internal discussion.",
        "Managerial notes: Performance reviews will start next week."
    ]

    
    critical_templates = [
        "URGENT: Transaction failed. Card details: 4242-5555-6666-7777.",
        "CONFIDENTIAL: Here is my IBAN: BG98KBCB91234567890123.",
        "Top Secret: The server root password is 'Admin!@#2026'.",
        "Financial Leak: Q3 revenue forecast shows a 15% drop.",
        "Customer Data: John Doe, SSN: 8501011234, Credit Card: 1111 2222 3333 4444.",
        "Encrypted key for the database is attached. DO NOT FORWARD."
    ]

    print(f"🚀 Generating {count} smart emails...")

    for i in range(count):
        filename = f"emails/mail_{i}.txt"
        
    
        choice = random.random()
        if choice < 0.6:
            content = random.choice(safe_templates)
        elif choice < 0.9:
            content = random.choice(warning_templates)
        else:
            
            content = random.choice(safe_templates) + " " + random.choice(critical_templates)

        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)

    print(f"✅ Created {count} files with diverse security scenarios.")

if __name__ == "__main__":
    generate_data(100)      

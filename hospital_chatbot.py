print("Welcome to Hospital Enquiry Chatbot!")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() in ["bye","exit","quit"]:
        print("Bot: Thank you for contacting us!")
        break

    elif "appointment" in user_input.lower() or "appointments" in user_input.lower():
        print("Bot: You can book an appointment by contacting the hospital reception.")

    elif "visit" in user_input.lower() or "visiting" in user_input.lower():
        print("Bot: Visiting hours are from 10 AM to 6 PM.")

    elif "emergency" in user_input.lower():
        print("Bot: For medical emergencies, please contact the hospital emergency department immediately.")

    elif "doctor" in user_input.lower() or "doctors" in user_input.lower():
        print("Bot: You can contact the hospital reception to get information about available doctors.")

    elif "room" in user_input.lower() or "rooms" in user_input.lower():
        print("Bot: Please contact the hospital reception for information about room availability.")

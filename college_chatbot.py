print("Welcome to College Enquiry Chatbot!")

while True:

    user_input = input("You: ").strip()

    if user_input.lower() in ["bye", "exit", "quit"]:
        print("Bot: Thank you for visiting!")
        break

    elif "courses" in user_input.lower():
        print("Bot: We offer various engineering courses: 1)Computer, 2) IT, 3)AIDS, 4)Mechanical.")

    elif "fees" in user_input.lower():
        print("Bot: Please contact the college office for fee details.")

    elif "timings" in user_input.lower():
        print("Bot: The College Timings are from 9AM to 4PM.")

    elif "admission" in user_input.lower():
        print("Bot: For admission details, please contact the college admission office.")

    elif "location" in user_input.lower():
        print("Bot: Our college is located in Manjari, Pune.")

    elif "contact" in user_input.lower():
        print("Bot: You can contact the college office for further infomation.")
        
    else:
        print("Bot: Sorry, I couldn't understand that. Please ask about courses, fees, admission, location, contact or timings.")


    

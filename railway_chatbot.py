print("Welcome to Railway Enquiry Chatbot!")

while True:

    user_input = input("You: ").strip()

    if user_input.lower() in ["bye","exit","quit"]:
        print("Bot: Thank you for using railway Enquiry!")
        break

    elif "timing" in user_input.lower() or "schedule" in user_input.lower():
        print("Bot: Please check the official railway timetable for train timings.")


    elif "train" in user_input.lower() or "trains" in user_input.lower():
        print("Bot:Please visit the railway Enquiry counter for train information.")

    elif "ticket" in user_input.lower() or "booking" in user_input.lower():
        print("Bot: You can book railway ticket through the official railway booking website .")

   
    elif "platform" in user_input.lower():
        print("Bot: Please check the station display boards for platform information.")

    elif "fare" in user_input.lower() or "price" in user_input.lower():
        print("Bot: Ticket fare depends on the train and travel class.")

    elif "status" in user_input.lower() or "pnr" in user_input.lower():
        print("Bot: You can check the PNR status through the official railway enquiry service.")

    elif "cancel" in user_input.lower():
        print("Bot: You can cancel your ticket through the railway booking service.")

    else:
        print("Bot: Sorry, I couldn't understand your question.")

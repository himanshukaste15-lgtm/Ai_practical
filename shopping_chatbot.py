print("Welcome to Online  Shopping  Assistant!")

while True:
    user_input = input("You: ").strip().lower()

    if user_input in ["bye","exit","quit"]:
        print("Bot: Thank you for shopping with us!")
        break

    elif "return" in user_input or "refund" in user_input:
        print("Bot: You can request  a return or refund through the orders section.")

    elif "track" in user_input or "order status" in user_input:
        print("Bot: You can track you order using you order ID.")

    elif "payment" in user_input or "pay" is user_input:
        print("Bot: we accept UPI,Debit card,Credit cards and net backing.")

    elif "delivery" in user_input or "shipping" in user_input:
        print("Bot: Delivery usually takes 3 to 7 working days.")

    elif "price" in user_input or "cost" in user_input:
        print("Bot: Product prices are displayed on their respective product pages.")

    elif "product" in user_input or "item" in user_input:
        print("Bot: We offer electronics, clothing, accessories and household products.")

    else:
        print("Bot: Sorry, I couldn't understand your question.")
        








    
    

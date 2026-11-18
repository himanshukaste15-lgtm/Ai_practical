#practical 1: Vacuum Cleaner Agent

#initialize the actions

def vacuum_agent(location, status):

                 if status =="Dirty":
                    return "Suck"

                 elif location =="A":
                    return "Move Right"

                 else:
                    return "Move Left"

#initialize the environment

rooms = {
    "A":"Dirty",
    "B":"Dirty"
    }
location ="A"

print("Initial State:",rooms)

#execute the agent

while "Dirty" in rooms.values():

    status = rooms[location]

    action = vacuum_agent(location,status)

    print("\nLocation:",location)
    print("Status:",status)
    print("Action:",action)

    if action =="Suck":
        rooms[location]="Clean"

    elif action =="Move Right":
        location = "B"

    elif action =="Move Left":
        location ="A"


print("\nFinal State:",rooms)
print("Both rooms are clean!")

    

    

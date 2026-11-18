def dfs():
   
    stack = [
        ((0,0,),[(0,0)])   
    ]
    visited = set()

    while stack:
        state,path = stack.pop()

        if state in visited:
            continue
        
        visited.add(state)

        if state ==(0,1):
            print("Solution Found:",path)
            
            return

        small, big = state

        next_states = [
            (2, big), #fill small jug
            (small,5), # fill big jug
            (0,big),  # empty small jug
            (small,0) # empty big jug
        ]

        #A) pour small jug into big jug
        amount = min(small, 5-big)
        next_states.append((small-amount, big+amount))

        #B) pour big jug into small jug
        amount = min(2-small, big)
        next_states.append((small+amount, big-amount))

        for new_state in next_states:
            if new_state not in visited:
                stack.append((new_state,path+[new_state]))

    print("No solution found")

dfs()

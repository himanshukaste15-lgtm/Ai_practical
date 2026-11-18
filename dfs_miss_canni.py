def is_valid(left_m,left_c):

    right_m = 3 - left_m
    right_c = 3 - left_c

    if left_m < 0 or left_c < 0 or left_m > 3 or left_c > 3:
        return False

    if left_m > 0 and left_m < left_c:
        return False

    if right_m > 0 and right_m < right_c:
        return False

    return True

def get_next_states(state):

    left_m,left_c,boat = state
    next_states = []

    moves = [ (1,0), (2,0), (0,1), (0,2), (1,1) ]

    for dm, dc in moves:

        if boat == 0:
            new_m = left_m - dm
            new_c = left_c - dc
            new_boat = 1

        else:
            new_m = left_m + dm 
            new_c = left_c + dc
            new_boat = 0

        if is_valid(new_m, new_c):
            next_states.append((new_m, new_c, new_boat))

    return next_states



def dfs():

    start = (3,3,0)
    goal = (0,0,1)

    stack = [(start, [start])]
    visited = set()

    while stack:

        state, path = stack.pop()

        if state in visited:
            continue

        visited.add(state)

        if state == goal:
            print("Solution found!")
            print("Path:",path)
            return

        for new_state in get_next_states(state):

            if new_state not in visited:
                stack.append((new_state,path + [new_state]))

    print("No solution found")

dfs()

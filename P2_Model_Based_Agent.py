#Model-Based Intelligent Agent

#1)Create the grid environment

grid = [

    ['S','.','#'],
    ['.','#','.'],
    ['.','.','G']

    ]

# Starting position
start = (0,0)

# Goal posititon
goal = (2,2)

#current position of robot
position = start

#internal memory
visited = set()

print("Starting Position:",position)
print("Goal Position:",goal)

# function to check valid movement

def is_valid(position):

    row,col = position

    if row<0 or row>=3:
        return False
    elif col<0 or col>=3:
        return False
    elif grid[row][col] =='#':
        return False
    elif position in visited:
        return False
    else:
        return True
    
# Possible movements

moves = [
    (1,0),  #down
    (0,1),  #Right
    (-1,0), #up
    (0,-1)  #left
    ]

#calculate the next position

def get_next_position(position,move):
    row = position[0] + move[0]
    col = position[1] + move[1]

    return(row,col)

def find_path(position):

    visited.add(position)

    if position == goal:
        return[position]

    for move in moves:

        new_position = get_next_position(position,move)

        if is_valid(new_position):

            path = find_path(new_position)

            if path:
                return[position]+path

    return none

path = find_path(start)


if path:

    print("Path found:")

    for position in path:
        print(position)

else:
    print("No path found")


    








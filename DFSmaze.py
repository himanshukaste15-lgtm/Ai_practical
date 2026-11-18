
def dfs():

    maze = [
        ['S', '0', '#', '0'],
        ['0', '0', '#', '0'],
        ['#', '0', '0', '0'],
        ['#', '#', '0', 'G']
    ]

    start = (0, 0)
    goal = (3, 3)

    stack = [(start, [start])]
    visited = set()

    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    while stack:

        position, path = stack.pop()
        r, c = position

        if position in visited:
            continue

        visited.add(position)

        if position == goal:
            print("Goal found!")
            print("Path:", path)
            return

        for dr, dc in moves:

            nr = r + dr
            nc = c + dc

            if (0 <= nr < len(maze) and
                0 <= nc < len(maze[0]) and
                maze[nr][nc] != '#' and
                (nr, nc) not in visited):

                stack.append(((nr, nc), path + [(nr, nc)]))

    print("No path found")


dfs()

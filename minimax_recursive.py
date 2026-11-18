tree = [
    [3, 12, 8],
    [2, 4, 6],
    [14, 5, 2]

]

def minimax(depth, node, is_max):

    if depth == 1:
        if is_max:
            return max(tree[node])
        else:
            return min(tree[node])

    if is_max:
        best = float('-inf')
        for i in range(3):
            value = minimax(1,i,False)
            best = max(best,value)

        return best

result = minimax(0,0,True)
print("Best score:",result)
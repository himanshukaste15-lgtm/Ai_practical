values = [2,3,5,9,0,1,7,5]

def alphabeta(depth, index, is_max, alpha, beta):

    if depth == 3:
        return values[index]

    if is_max:
        best = float('-inf')

        for i in range(2):

            value = alphabeta(depth + 1, index * 2+i, False, alpha,beta)

            best = max(best, value)
            alpha = max(alpha,best)

            if beta<=alpha:
                break

        return best

    else:

        best = float('inf')

        for i in range(2):

            value = alphabeta(depth + 1, index * 2 + i,
                              True, alpha, beta)

            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best    

result = alphabeta(0,0,True,float('-inf'),float('inf'))
print("Optimal value:",result)

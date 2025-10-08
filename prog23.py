def alphabeta(depth, nodeIndex, isMax, scores, alpha, beta, h):
    if depth == h:
        return scores[nodeIndex]

    if isMax:
        best = -9999
        for i in range(2):
            val = alphabeta(depth+1, nodeIndex*2+i, False, scores, alpha, beta, h)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = 9999
        for i in range(2):
            val = alphabeta(depth+1, nodeIndex*2+i, True, scores, alpha, beta, h)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

# Example tree (leaf scores)
scores = [3, 5, 6, 9, 1, 2, 0, -1]
height = 3
print("Best value (with Alpha-Beta Pruning):", alphabeta(0, 0, True, scores, -9999, 9999, height))

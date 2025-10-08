def minimax(depth, isMaximizing, scores, h):
    if depth == h:
        return scores[depth]

    if isMaximizing:
        return max(minimax(depth+1, False, scores, h),
                   minimax(depth+1, False, scores, h))
    else:
        return min(minimax(depth+1, True, scores, h),
                   minimax(depth+1, True, scores, h))

# Example game tree (leaf node scores)
scores = [3, 5, 2, 9]
height = len(scores) - 1
print("Best score for maximizer:", minimax(0, True, scores, height))

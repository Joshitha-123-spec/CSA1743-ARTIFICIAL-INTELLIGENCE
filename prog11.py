N=8
def is_safe(board,row,col):
    for i in range(row):
        if board[i]==col or abs(board[i]-col)==abs(i-row):
            return False
    return True

def solve(row,board):
    if row==N:
        print(board); return True
    for col in range(N):
        if is_safe(board,row,col):
            board[row]=col
            if solve(row+1,board): return True
    return False

solve(0,[-1]*N)

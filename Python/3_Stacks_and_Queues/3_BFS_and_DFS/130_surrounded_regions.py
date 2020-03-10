# https://leetcode.com/problems/surrounded-regions/
# 130. Surrounded Regions
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
# Example:
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:
# X X X X
# X X X X
# X X X X
# X O X X
# Explanation:
# Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

# BFS Queue
def solve(board):
    # Do not return anything, modify board in-place
     if not board or not board[0]:
        return
    R, C = len(board), len(board[0])
    if R <= 2 or C <= 2:
        return
    q = []
    # start from the boarder and replace all O to N
    # put all the boarder value into queue.
    for r in range(R):
        q.append((r, 0))
        q.append((r, C-1))
    for c in range(C):
        q.append((0, c))
        q.append((R-1, c))
    while q:
        r, c = q.pop(0)
        if 0<=r<R and 0<=c<C and board[r][c] == "O":
            # modify the value from O to N
            board[r][c] = "N"
            # append the surrouding cells to queue.
            q.append((r, c+1))
            q.append((r, c-1))
            q.append((r-1, c))
            q.append((r+1, c))
    # replace all the O to X, then replace all the N to O
    for r in range(R):
        for c in range(C):
            if board[r][c] == "O":
                board[r][c] = "X"
            if board[r][c] == "N":
                board[r][c] = "O"

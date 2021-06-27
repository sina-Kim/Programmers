from itertools import product

def solution(board):
    width  = len(board[0])
    height = len(board)
    result = 0
    
    for h, w in product(range(1, height), range(1, width)):
        if board[h][w] == 0:
            continue
        value = min(board[h-1][w], board[h][w-1], board[h-1][w-1])
        board[h][w] += value
        result = max(result, board[h][w])
    
    if result == 0:
        if (1 in board[0]) or (1 in [row[0] for row in board]):
            result = 1
    
    return result**2
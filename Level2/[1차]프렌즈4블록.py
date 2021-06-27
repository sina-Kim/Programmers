import itertools

def solution(row, col, board):
    BLANK = ' '
    def is_ok(r, c):
        return (not board[r][c] == BLANK) and (
               board[r][c]     == \
               board[r+1][c]   == \
               board[r][c+1]   == \
               board[r+1][c+1])
    
    def to_blank(r, c):
        board[r][c]     = BLANK
        board[r+1][c]   = BLANK
        board[r][c+1]   = BLANK
        board[r+1][c+1] = BLANK
    
    def to_gravity():
        count_word = 0
        for c in range(0, col):
            alpha = []
            for r in range(row-1, -1, -1):
                if not board[r][c] == BLANK:
                    alpha.append(board[r][c])
                    board[r][c] = BLANK
            count_word += len(alpha)
            for r, v in zip(range(row-1, -1, -1), alpha):
                board[r][c] = v
        return count_word
    
    board  = [list(row) for row in board]
    word_count = row * col
    while True:
        points = []
        for r, c in itertools.product(range(row-1), range(col-1)):
            if is_ok(r, c):
                points.append((r, c))

        if points:    
            for point in points:
                to_blank(*point)
            word_count = to_gravity()
        else:
            return row * col - word_count
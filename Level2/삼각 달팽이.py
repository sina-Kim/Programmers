import collections
import itertools

def solution(n):
    answer = [[0] * length for length in range(1, n+1)]
    Coord = collections.namedtuple('Coord', 'row col')
    coord = Coord(0, 0)
    
    go_down    = lambda coord: Coord(coord.row+1, coord.col)
    go_right   = lambda coord: Coord(coord.row, coord.col+1)
    go_left_up = lambda coord: Coord(coord.row-1, coord.col-1)
    go_cycle   = itertools.cycle([go_down, go_right, go_left_up])
    go = next(go_cycle)
    
    total = (n * (n+1) // 2) + 1
    for value in range(1, total):
        answer[coord.row][coord.col] = value
        next_coord = go(coord)
        try:
            if answer[next_coord.row][next_coord.col]:
                raise ValueError("")            
        except:
            go = next(go_cycle)
            next_coord = go(coord)
            
        coord = next_coord
        
    return list(itertools.chain(*answer))
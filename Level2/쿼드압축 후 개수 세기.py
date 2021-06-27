import math

def solution(arr):
    result = [0, 0, 0]
    def inner_function(row, col, length):
        if length == 1:
            return arr[row][col]
        half = length // 2
        v1 = inner_function(row, col, half)
        v2 = inner_function(row+half, col, half)
        v3 = inner_function(row, col+half, half)
        v4 = inner_function(row+half, col+half, half)
        
        if v1 == v2 == v3 == v4:
            if v1 in (0, 1):
                return v1
        for v in (v1, v2, v3, v4):
            result[v] += 1
        return 2
    last = inner_function(0, 0, len(arr))
    result[last] += 1
    return result[0:2]
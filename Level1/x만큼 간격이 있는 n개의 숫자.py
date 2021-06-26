def solution(x, n):
    if x == 0:
        return [x] * n
    return list(range(x,x*n+(1 if x > 0 else -1),x))
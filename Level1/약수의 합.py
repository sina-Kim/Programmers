
def solution(n):
    return sum((factor for factor in range(1, n+1) if n % factor == 0))
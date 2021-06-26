def solution(x):
    value = sum(map(int, str(x)))
    return x % value == 0
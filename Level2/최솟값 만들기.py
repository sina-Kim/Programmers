def solution(A,B):
    A = sorted(A, reverse=True)
    B = sorted(B)
    acc = 0
    for a, b in zip(A, B):
        acc += a * b

    return acc
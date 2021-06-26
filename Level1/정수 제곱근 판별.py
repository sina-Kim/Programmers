def solution(n):
    from math import sqrt
    root = sqrt(n)
    return (int(root)+1)**2 if root == int(root) else -1
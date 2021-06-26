def solution(n, m):
    import math
    gcd = math.gcd(n, m)
    return [gcd, n * m // gcd]
def solution(n):
    cache = [-1 for _ in range(n+1)]
    cache[0] = 0
    cache[1] = 1
    
    for index in range(2, n+1):
        cache[index] = cache[index-1] + cache[index-2]
    
    return cache[n] % 1234567

## other solution

from functools import lru_cache
@lru_cache(100000)
def solution(n):
    if n == 0 or n == 1:  return n
    return solution(n-1) + solution(n-2)
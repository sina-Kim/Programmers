import math

def solution(n):
    answer = 1
    m = 2 * n
    for x in range(1, n//2+2):
        for y in range(x+1, n):
            calc = y**2 - x**2 + x + y
            
            if calc == m:
                answer += 1
                break
            elif calc > m:
                break
    
    return answer
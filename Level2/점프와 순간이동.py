import array

def solution(n):
    count = 1
    while True:
        while n % 2 == 0:
            n = n // 2
        if n == 1:
            return count
        n -= 1
        count += 1
        
    return count
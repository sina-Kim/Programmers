
def solution(n):
    is_prime = {integer: 1 for integer in range(1, n+1)}
    is_prime[1] = 0
    for integer in range(2, n+1):
        if is_prime[integer]:
            for multiple in range(integer*2, n+1, integer):
                is_prime[multiple] = 0
    
    return sum(is_prime.values())
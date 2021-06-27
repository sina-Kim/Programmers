import itertools
import collections

def is_prime(value):
    import math
    if value < 2:
        return False
    if value in (2, 3):
        return True
    
    if value % 2 == 0:
        return False
    
    for idx in range(3, int(math.sqrt(value))+1, 2):
        if value % idx == 0:
            return False
    return True

def solution(numbers):
    
    numbers = list(numbers)
    permutation = []    
    length = len(numbers) if len(numbers) <= 7 else 7        
    for index in range(1, length + 1):
        permutation.append(itertools.permutations(numbers, index))
        
    result  = collections.defaultdict(int)
    count   = 0
    
    for value in itertools.chain(*permutation):
        value = int(''.join(value))
        if result[value] == 0 and is_prime(value):
            result[value] = 1
            count += 1
                   
    return count
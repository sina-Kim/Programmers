from functools import reduce

def solution(a, b):
    '''
    Args:
        a: List[Int]: vector of integers
        b: List[Int]: vector of integers
        * len(a) == len(b) is always True
    Returns:
        Int: dot product of a, b
    '''
    return reduce(lambda x, y: x + y,
                  (a1 * b1 for a1, b1 in zip(a, b)))
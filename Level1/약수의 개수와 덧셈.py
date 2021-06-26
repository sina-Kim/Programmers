from math import sqrt, ceil

def get_number_of_factors(left, right):
    factors = {integer: 1 for integer in range(left, right+1)}
    for factor in range(2, right+1):
        for integer in range(factor, right+1, factor):
            if left <= integer <= right:
                factors[integer] += 1

    return factors
    


def solution(left, right):
    '''
    Args:
        left: Int
        right: Int
        * range of integers
    Returns:
        Int: count number when number of factor is even
    '''
    number_of_factors = get_number_of_factors(left, right)
    result = 0
    for key, value in number_of_factors.items():
        if value % 2 == 0:
            result += key
        else:
            result -= key
    return result

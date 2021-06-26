def base10_to_3(n):
    'base 10 to base 3 (reversed)'
    result = ''
    while n:
        n, rest = divmod(n, 3)
        result += str(rest)
    return result

def solution(n):
    '''
    Args:
        n: Int
    Returns:
        Int
    '''
    reversed_base3 = base10_to_3(n)
    return int(reversed_base3, base=3)
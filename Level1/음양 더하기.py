def solution(absolutes, signs):
    '''
    Args:
        absolutes: List[Unsigned Int]
        signs: List[Bool]
    Returns:
        Int
    '''
    result = 0
    for absolute, sign in zip(absolutes, map(lambda x: 1 if x else -1, signs)):
        result += sign * absolute
    return result
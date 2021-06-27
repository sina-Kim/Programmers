def solution(n: int, a: int, b: int):
    '''
    Args:
        n: 대회에 참가하는 사람의 수
        a: 1번 참가자의 번호
        b: 2번 참가자의 번호
    Returns:

    '''
    count, a, b = 1, a - 1, b - 1
    if a > b:
        a, b = b, a
    while not (a % 2 == 0 and b - a == 1):        
        count += 1
        a, b = a>>1, b>>1
        
    return count
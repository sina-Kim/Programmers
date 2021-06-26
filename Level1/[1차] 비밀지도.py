def get(value, n):
    for _ in range(n):
        yield '#' if value & 1 else ' '
        value >>= 1

def solution(n, arr1, arr2):
    '''
    Args:
        n: Int: 지도의 크기
        arr1: List[Int]: 암호 1
        arr2: List[Int]: 암호 2
    Returns:
        List[str]: 완성된 지도
        * 벽은 " ", 빈 곳은 " "으로 표기
    '''
    return [''.join(get(x | y, n))[::-1] for x, y in zip(arr1, arr2)]
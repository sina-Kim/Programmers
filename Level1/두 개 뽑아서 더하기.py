from itertools import permutations

def solution(numbers):
    '''
    Args:
        numbers: List[Int]: 정수 목록
    Returns:
        List[Int]
    '''
    answer = set()
    for left, right in permutations(numbers, 2):
        answer.add(left + right)
    return sorted(list(answer))

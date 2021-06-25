def solution(nums):
    '''
    Args:
        nums: List[int]: 폰켓몬의 번호
    Returns:
        int: 최대로 가져갈 수 있는 서로 다른 포켓몬의 수
    '''
    from collections import Counter
    counter = Counter(nums)
    if len(counter) >= len(nums)//2:
        return len(nums)//2
    else:
        return len(counter)


from itertools import combinations

def solution(nums):
    '''
    Args
        nums: List[int]: list of integers 
        * 1<= x <= 1000
        * No duplicates
    Returns
        int: number of primes made from three numbers
    '''
    # 숫자 정렬 후 최대 크기의 숫자 계산
    nums.sort()
    max_sum = sum(nums[-3:])
    # 소수 판별을 위한 딕셔너리 생성
    is_primes = {integer: True for integer in range(1, max_sum+1)}
    is_primes[1] = False
    for idx in range(2, max_sum+1):
        for jdx in range(idx+idx, max_sum+1, idx):
            is_primes[jdx] = False

    # 각 조합에 따른 소수 개수 확인
    count = 0
    for a, b, c in combinations(nums, 3):
        count += int(is_primes[a+b+c])
    return count
    

    
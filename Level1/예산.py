def solution(d, budget):
    '''
    Args:
        d: List[Int]: 부서별 신청 금액이 들어있는 벡터
        budget: Int: 총 예산
    Returns:
        Int: 지원해줄 수 있는 최대 부서 수
    '''
    for count, money in enumerate(sorted(d)):
        budget -= money
        if budget < 0:
            return count
    return len(d)
from collections import Counter

def solution(N, stages):
    '''
    Args:
        N: Int:  총 스테이지의 개수
        stages: List[Int]: 각 스테이지 별 멈춰있는 사용자의 수\
    Returns:
        List[Int]: 실패율 기준 내림차순 정렬된 스테이지
    '''
    counter = Counter(stages)
    result  = dict()

    players = len(stages)
    for stage in range(1, N+1):
        reached = counter[stage] if stage in counter else 0
        failure = (reached / players) if players != 0 else 0
        players -= reached
        result[stage] = failure
    
    return [stage for stage, failure in 
    sorted(result.items(), key=lambda x:x[1], reverse=True)]
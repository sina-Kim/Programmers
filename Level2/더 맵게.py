from typing import List
from heapq  import heapify, heappop, heappush

def solution(scoville: List[int], K: int):
    '''
    Args:
        scoville: 길이 2이상 1,000,000 이하
                : 각 원소는 0이상 1,000,000 이하
        K       : 특정 스코빌 값
    Returns:
        int: 모든 음식의 스코빌 값을 K 이상으로 만들기 위해 섞어야 하는 횟수
           : 불가능하다면 -1 반환
    '''
    count = 0
    heapify(scoville)  # min heap

    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        
        minf, mins = heappop(scoville), heappop(scoville)
        heappush(scoville, minf + mins * 2)
        count += 1
    
    return count
        

from collections import deque
from math        import ceil
from typing      import List

def solution(progresses: List[int], speeds: List[int]):
    '''
    Args:
        progress: 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열
        speeds: 각 작업의 개발 속도가 정힌 정수 배열
    Returns:
        List[int]: 각 배포마다 몇 개의 기능이 배포되는지 적히 리스트
        * 단, 배포는 하루에 한 번 가능하며
        * 앞선 기능이 배포되기 전까지 다음 기능을 배포할 수 없다.
    '''
    queue = deque([(progress, speed)  \
                   for progress, speed in zip(progresses, speeds)])
    function = 0     # 개발된 기능 개수
    distribute = []  # 배포

    # queue에 남은 원소가 있을 때 까지 반복
    while queue:
        # 가장 앞선 기능이 배포될 때까지 필요한 날짜 계산
        progress, speed = queue.popleft()
        day = ceil((100 - progress) / speed)
        function = 1
        
        # 앞선 기능이 개발되었을 때 함께 개발된 기능의 개수 확인
        while queue:
            progress, speed = queue[0]
            if progress + (speed * day) >= 100:
                function += 1
                queue.popleft()
            else:
                break
        
        # 기능의 개수를 배포 목록에 추가
        distribute.append(function)
    return distribute
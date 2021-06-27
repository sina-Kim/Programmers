def dfs(numbers, exit_condition, target_value):
    def __inner__(condition, value):
        # 내부 함수에서 numbers, exit_condition, target_value를 참조한다.
        # exit condition과 target value가 일치한다면 1을 반환한다.
        if condition == exit_condition:
            if value == target_value:
                return 1
            return 0
        # dfs로 모든 경우를 탐색한다.
        return __inner__(condition+1, value+numbers[condition]) +  \
               __inner__(condition+1, value-numbers[condition])
    return __inner__

def solution(numbers, target):
    '''
    Args:
        numbers: List[Int]: 사용할 수 있는 숫자가 담긴 배열
        * 0 <= numbers[X]
        * 2 <= len(numbers) <= 20
        target: Int: 목표 숫자
    Returns:
        Int: target을 달성할 수 있는 조합의 수
    '''
    _solution = dfs(numbers, len(numbers), target)
    return _solution(0, 0)
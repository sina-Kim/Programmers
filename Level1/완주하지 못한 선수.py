def solution(participant, completion):
    """
    Args:
        participant : 마라톤에 참여한 선수들의 이름이 담긴 배열
        completion  : 완주한 선수들의 이름이 담긴 배열
        * 참가자 중 동명이인이 있을 수 있다.
        * completion의 길이는 participant의 길이보다 1 작다.
    Returns:
        str: 완주하지 못한 선수의 이름
    """
    # 이름 순 정렬
    participant.sort()
    completion.sort()

    # 순회하며 이름을 조회하고 다르다면 출력
    for (x, y) in zip(participant, completion):
        if not x == y:
            return x
    # 만약 조건문에서 걸러지지 않는다면 참가자 중 가장 마지막 순서의
    # 이름을 가진 사람이 완주하지 못한 선수
    return participant[-1]


if __name__ == '__main__':
    participant = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]
    result = solution(participant, completion)
    print(result)
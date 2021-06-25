from itertools import cycle

def solution(answers):
    '''
    Args:
        answers: List[int]: 정답 목록
    Returns:
        int: 각 수포자 중 가장 많이 맞힌 사람의 번호
        * 가장 높은 점수를 받은 사람이 여럿일 경우
        * 오름차순으로 정렬하여 반환
    '''

    # 각 패턴을 무한히 반복할 수 있는 순회가능 객체 생성
    pattern = [
        cycle(map(int, '1 2 3 4 5'.split())),
        cycle(map(int, '2 1 2 3 2 4 2 5'.split())),
        cycle(map(int, '3 3 1 1 2 2 4 4 5 5'.split()))
    ]

    # 각 패턴 별 학생 점수를 기록
    student = [0 for _ in range(3)]
    for score in answers:
        if score == next(pattern[0]):  student[0] += 1
        if score == next(pattern[1]):  student[1] += 1
        if score == next(pattern[2]):  student[2] += 1

    max_score = max(student)
    return [index+1 for index, score in enumerate(student) if score == max_score]

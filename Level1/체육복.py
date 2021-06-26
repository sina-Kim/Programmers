def solution(n, lost, reserve):
    '''
    Args:
        n: Int: Total number of students
        lost: List[Int]: Student ID whose gym uniform was stolen
        reserve: List[Int]: Student ID with a spare gym uniform
    Returns
        Int: The maximum number of students who can take PE classes.
    '''
    _lost, _reserve = set(lost), set(reserve)
    lost    = _lost - _reserve  # 여분도 없는 학생
    reserve = _reserve - _lost  # 여분이 있는 학생

    # 여분이 있는 학생을 순회
    for rs in reserve:
        # 만약 앞 뒤 학생에 여분도 없는 학생이 있다면
        # 대여해준다. (lost.remove(stduent))
        if rs - 1 in lost:
            lost.remove(rs - 1)
        elif rs + 1 in lost:
            lost.remove(rs + 1)

    # 대여 과정이 끝나고도 의상이 없는 학생 수를
    # 전체 학생 수에서 빼준다.
    return n - len(lost)
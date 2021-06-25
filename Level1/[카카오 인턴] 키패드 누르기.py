KEYPAD = { 1: (1, 1), 2: (1, 2), 3: (1, 3),
           4: (2, 1), 5: (2, 2), 6: (2, 3),
           7: (3, 1), 8: (3, 2), 9: (3, 3),
                      0: (4, 2)             }

LEFT, RIGHT = 0, 1

# 맨하튼 거리를 계산
def distance(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def solution(numbers, hand):
    '''
    Args:
        numbers: List[int]: 눌러야할 번호의 순서 목록
        hand: str         : 왼손잡이/오른손잡이를 나타내는 인자
        * (1, 4, 7)은 왼손으로 누른다.
        * (3, 6, 9)는 오른손으로 누른다.
        * (2, 5, 8, 0)은 가까운 손으로 누른다.
    Returns:
        str: 각 번호를 누르는 손을 L/R을 통해 표현
        * ex) LRLLLRLLRRL
    '''
    result = ''
    hand = LEFT if hand == 'left' else RIGHT
    SIDE = [(1, 4, 7), (3, 6, 9)]
    FINGER = [(4, 1), (4, 3)]
    VALUE = ["L", "R"]

    # 손가락의 위치를 변경하고 해당하는 문자를 반환
    def move(side):
        FINGER[side] = KEYPAD[number]
        return VALUE[side]

    # 눌러야할 번호를 순회
    for number in numbers:
        # 왼쪽이나 오른쪽에 있다면 이동
        if   number in SIDE[LEFT]  :  result += move(LEFT)
        elif number in SIDE[RIGHT] :  result += move(RIGHT)
        else:
            # 가운데 줄이라면 거리를 계산하여 이동
            ldist = distance(FINGER[LEFT], KEYPAD[number])
            rdist = distance(FINGER[RIGHT], KEYPAD[number])
            if   ldist < rdist :  result += move(LEFT)
            elif ldist > rdist :  result += move(RIGHT)
            else               :  result += move(hand)          

    return result
            
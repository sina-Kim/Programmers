RANK = [6, 6, 5, 4, 3, 2, 1]

def solution(lottos, win_nums):
    '''
    Args
        lottos: List[int]: 로또 추첨 번호
                         : 지워진 번호는 0으로 표현
        win_nums: List[int]: 로또 당첨 번호
    Return
        최대 등수, 최소 등수
    '''
    global RANK

    lottos   = set(lottos) - {0}            # 확인 가능한 추첨 번호
    win_nums = set(win_nums)                # 당첨 번호
    match_count = len(win_nums & lottos)    # 일치(match)한 번호의 개수
    zero_count  = 6 - len(lottos)           # 지워진 번호의 개수
    return [RANK[match_count + zero_count], RANK[match_count]]
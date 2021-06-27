def solution(s: str):
    '''
    Args:
        s: 튜플의 표기법이 문자열 형태로 주어집니다.
        * ex) "{{2},{2,1},{2,1,3},{2,1,3,4}}"
    Returns:
        List[int]: 튜플을 리스트 형태로 반환합니다.
    '''
    # s[2:-2].split('},{')  => ['2', '2,1', '2,1,3', '2,1,3,4']
    # set(map(int, x.split(','))) => [{2}, {2, 1}, {2, 1, 3}, {2, 1, 3, 4}]
    list_of_set = list(map(lambda x: set(map(int, x.split(','))), s[2:-2].split('},{')))
    # 원소의 개수를 기준으로 정렬
    list_of_set.sort(key=len)
    result = []
    
    for some_set in list_of_set:
        diff_set = some_set - set(result)
        result.append(diff_set.pop())
        
    return result
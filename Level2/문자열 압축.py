def tokenize(string: str, unit: int):
    '''
    Args:
        string: 입력 문자열
        unit: 분할 단위
    Yield:
        str: unit 크기의 조각난 문자열
    '''
    while string:
        token, string = string[0:unit], string[unit:]
        yield token

def compress(string: str, unit: int):
    '''
    Args:
        string: 입력 문자열
        unit: 압축 단위
    Returns:
        int: 압축된 문자열의 크기
    '''
    answer = 0
    
    # rest에 따라 토큰의 개수가 달라짐
    share, rest = divmod(len(string), unit)
    start, end  = 1, share + 1 if rest else share
    
    token_get = iter(tokenize(string, unit))
    count     = 1
    token     = next(token_get)
    for _ in range(start, end):
        ntoken = next(token_get)
        # 이전 토큰과 다음 토큰이 같다면 압축
        if token == ntoken:
            count += 1
        else:
            answer += unit
            answer += (0 if count == 1 else len(str(count)))
            token   = ntoken
            count   = 1

    answer += len(token)
    answer += (0 if count == 1 else len(str(count)))
    return answer

def solution(string: str):
    '''
    Args:
        string: 입력된 문자열
    Returns:
        int: 압축된 문자열 중 가장 짧은 문자열의 길이
    '''
    start  = 1                  # 압축 가능한 최소 단위
    end    = len(string) // 2   # 압축 가능한 최대 단위
    answer = len(string)
    
    # 모든 압축 가능한 단위, unit에 대해서 반복
    for unit in range(start, end + 1):
        length = compress(string, unit)  # 압축
        answer = min(answer, length)     # 정답을 최소값으로 갱신
    return answer
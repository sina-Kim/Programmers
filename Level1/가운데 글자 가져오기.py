def solution(s):
    '''
    Args:
        s: str: 길이가 1이상, 100이하인 문자열
    Returns:
        str: 각 문자열의 가운데 글자
    '''
    length = len(s)//2
    return s[length-1:length+1] if len(s)%2 == 0 else s[length]
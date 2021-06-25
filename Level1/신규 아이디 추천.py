import re

def solution(new_id):
    '''
    Args:
        new_id: str: 신규 아이디
    Returns:
        str: 추천 아이디
    '''
    #  알파벳 대문자를 알파벳 소문자로 변환
    recommend_id = new_id.lower()
    #  알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    recommend_id = re.sub('[^a-z0-9\-\_\.]', '', recommend_id)
    #  두 개 이상 연속된 .을 하나로 변경
    recommend_id = re.sub('\.\.+', '.', recommend_id)
    #  . 이 맨 처음이나 끝에 위치한다면 제거
    recommend_id = re.sub('^\.|\.$', '', recommend_id)

    #  빈 문자열이라면 'a'를 삽입
    if not recommend_id:
        recommend_id = 'a'

    #  문자열을 길이를 15개까지로 자르고 마지막이 . 이라면 제거한다.
    recommend_id = re.sub('\.$', '', recommend_id[:15])
    #  만약 길이가 3보다 작다면 마지막 글자를 연속해서 붙인다.
    while len(recommend_id) < 3:
        recommend_id += recommend_id[-1]
    return recommend_id
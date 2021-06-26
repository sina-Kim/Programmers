import datetime

def solution(month, day):
    '''
    Args:
        month: Int: month of 2016
        day: Int: day of 2016
    Returns:
        str: weeknd
    '''
    dt = datetime.datetime(2016, month, day)
    return 'MON,TUE,WED,THU,FFRI,SAT,SUN'.split(',')[dt.weekday()]
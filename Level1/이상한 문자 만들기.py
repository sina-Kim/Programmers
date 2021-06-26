def function(s):    
    for word in s.split(' '):
        result = ''
        for index, char in enumerate(word):
            if index % 2 == 0:  result += char.upper()
            else:               result += char.lower()
        yield result

def solution(s):
    '''
    Args:
        s: str
    Returns:
        str
    '''
    return ' '.join(function(s))
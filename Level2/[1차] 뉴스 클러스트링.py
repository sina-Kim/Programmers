from collections import Counter

def break_in_2pieces(string):
    word = ''
    for char in string:
        word += char.lower()
        word = word[-2::]
        
        if len(word) == 2 and word.isalpha():
            yield word

def J(multiset1, multiset2):
    union = 0
    intersect = 0
    for keyword, value1 in multiset1.items():
        if keyword in multiset2:
            value2 = multiset2[keyword]
            del multiset2[keyword]
        else:
            value2 = 0
            
        union += max(value1, value2)
        intersect += min(value1, value2)
    
    for keyword, value2 in multiset2.items():
        union += value2
    
    if union == 0:
        return 1    
    return intersect / union
            
def solution(str1, str2):
    multiset1 = Counter(break_in_2pieces(str1))
    multiset2 = Counter(break_in_2pieces(str2))
    return int(J(multiset1, multiset2) * 65536)
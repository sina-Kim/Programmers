from collections import deque

bonus2int = {
    'S' : 1,
    'D' : 2,
    'T' : 3
}

def getInt(dartResult: deque):
    parse = ''
    while '0' <= dartResult[0] <= '9':
        parse += dartResult.popleft()
    return int(parse)
    
def getBonus(dartResult):
    global bonus2int
    bonus = dartResult.popleft()
    return bonus2int[bonus]
    
def getOption(dartResult):
    return dartResult.popleft()
    
def isOption(dartResult):
    return dartResult[0] in "*#"
    
def solution(dartResult):
    dartResult = deque(dartResult)
    total  = 0
    before = 0
    while dartResult:
        score = getInt(dartResult)
        bonus = getBonus(dartResult)
        score **= bonus
        if dartResult and isOption(dartResult):
            option = getOption(dartResult)
            if option == "*":
                total += before
                score *= 2
            else:
                score *= -1
        before = score
        total += score
    return total
            
    
    
    return total
def solution(num):
    operate = (
        lambda x: x//2,
        lambda x: x*3+1
    )
    
    for i in range(0, 500):
        if num == 1:
            return i
        num = operate[num & 1](num)
        
    return -1
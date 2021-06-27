def solution(s):
    count = 0
    removed_zero = 0
    
    while not s == "1":
        # 이진변환 횟수 update
        count += 1
        x = ''.join(s.split('0'))
        c = len(x)
        # 제거된 0의 개수 update
        removed_zero += (len(s) - c)
        s = "{0:b}".format(c)
    
    return [count, removed_zero]
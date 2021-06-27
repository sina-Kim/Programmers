def solution(s):
    cnt = 0
    for ch in s:
        if(cnt < 0): break  
        if ch == '(': cnt+= 1
        else: cnt-=1

    return cnt==0
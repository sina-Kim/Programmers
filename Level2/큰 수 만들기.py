def solution(number, k):
    pos = 0
    while k:
        if pos+1 == len(number):
            number = number[:-k]
            break
            
        if number[pos] >= number[pos+1]:
            pos += 1
        else:
            number = number[:pos] + number[pos+1:]
            k -= 1
            pos = pos - 1 if pos else pos
    return number
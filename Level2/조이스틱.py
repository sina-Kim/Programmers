def solution(name):
    cache = [min(ord(alpha) - ord('A'), ord('Z') - ord(alpha) + 1) for alpha in name]
    lt, rt = 0, 0
    move   = 0
    index  = 0
    while True:
        move += cache[index]
        cache[index] = 0
        if sum(cache) == 0:
            break
        lt, rt = 1, 1
        while cache[index-lt] == 0:
            lt += 1
        while cache[index+rt] == 0:
            rt += 1
        move += lt if lt < rt else rt
        index += -lt if lt < rt else rt
        
    return move
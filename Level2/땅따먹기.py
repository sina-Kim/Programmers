def solution(land):
    COL = 0
    VAL = 1
    # cache 초기화
    cache = [[0] * 4 for _ in land]
    cache[0] = land[0].copy()

    for current_index in range(1, len(land)):
        before_index = current_index - 1
        before_cache = sorted(list(enumerate(cache[before_index])), reverse=True, key=lambda x: x[1])
        a, b = before_cache[0:2]
        
        for col in range(4):
            if col == a[COL]:
                cache[current_index][col] = b[VAL] + land[current_index][col]
            else:
                cache[current_index][col] = a[VAL] + land[current_index][col]

    return max(cache[-1])
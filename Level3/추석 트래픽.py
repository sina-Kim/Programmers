def preprocess_end(s):
    h, m, s = s.split(':')
    return int(int(h) * 3600000 + int(m) * 60000 + float(s)*1000)

def preprocess_pro(s):
    return int(float(s[:-1]) * 1000)

def solution(lines):
    start_ends = []
    for line in lines:
        _, end, process = line.split(' ')
        
        end   = preprocess_end(end)
        start = end - preprocess_pro(process) + 1
        start_ends.append((start, end))
    max_cnt = -1
    print(start_ends)
    for start, end in start_ends:
        cs, ce = len(start_ends), len(start_ends)

        for start2, end2 in start_ends:
            if start > end2 or start+999 < start2:
                cs -= 1
            if end > end2 or end+999 < start2:
                ce -= 1
                
        max_cnt = cs if max_cnt < cs else max_cnt
        max_cnt = ce if max_cnt < ce else max_cnt

    return max_cnt
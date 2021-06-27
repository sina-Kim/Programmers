import collections

def solution(citations):
    h_index = 0
    citations = sorted(citations, reverse=True)
    while h_index < len(citations):
        if citations[h_index] <= h_index:
            break
        h_index += 1
    return h_index
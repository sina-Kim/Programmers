import itertools

def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def get_next_value(base, count, people):
    repeat = (count + 1) * people
    for number in itertools.count(0):
        for char in convert(number, base=base):
            repeat -= 1
            if repeat == 0:
                return char
            yield char
            
def solution(base, count, people, pos):
    return ''.join(list(get_next_value(base, count, people))[pos-1::people][:count])
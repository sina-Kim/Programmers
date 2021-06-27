def solution(n):
    get_one = lambda x: len(list(filter(lambda y: y=='1', '{0:b}'.format(x))))
    limit = get_one(n)
    while True:
        n += 1
        if get_one(n) == limit:
            return n
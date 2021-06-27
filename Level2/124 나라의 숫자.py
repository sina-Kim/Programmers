def solution(n):
    answer = ''
    while n > 0:
        n, r = divmod(n - 1, 3)
        answer = ('1', '2', '4')[r] + answer
    return answer
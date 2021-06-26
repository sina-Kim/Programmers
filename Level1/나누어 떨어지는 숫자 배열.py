def solution(arr, divisor):
    answer = [element for element in arr if not element % divisor]
    return sorted(answer) if answer else [-1]
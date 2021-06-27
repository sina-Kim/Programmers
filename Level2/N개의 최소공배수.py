def greatest_common_divisor(a, b):
    while(b > 0):
        a, b = b, a % b
    return a

def least_common_multiple(a, b):
    return (a * b) // greatest_common_divisor(a, b)

def solution(arr):
    while len(arr) > 1:
        a = arr.pop()
        b = arr.pop()
        arr.append(least_common_multiple(a, b))
    return arr[0]
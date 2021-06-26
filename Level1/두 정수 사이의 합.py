def solution(num1, num2):
    if num1 <= num2:
        return int(num2*(num2+1)/2 - abs((num1*(num1-1)/2)))
    else:
        return solution(num2, num1)
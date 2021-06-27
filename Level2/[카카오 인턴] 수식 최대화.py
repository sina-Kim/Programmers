import itertools
import copy

def calculator(expression, order):
    def get_value():
        if order[0] == '-':
            return handle[-1] - v
        elif order[0] == '+':
            return handle[-1] + v
        else:
            return handle[-1] * v
    handle = list()
    next_h = expression
    flag = False
    while order:
        for v in next_h:
            if v == order[0]:
                flag = True
            elif flag:
                handle[-1] = get_value()
                flag = False
            else:
                handle.append(v)
        next_h = handle
        handle = []
        order.pop(0)
    return abs(next_h[0])
                

def solution(expression):
    def make_list():
        result = []
        value  = ''
        for ch in expression:
            if ord('0') <= ord(ch) <= ord('9'):
                value += ch
            else:
                result.append(int(value))
                result.append(ch)
                value = ''
        result.append(int(value))
        return result
    
    expression_list = make_list()
    
    value  = 0
    answer = -987654321
    for order in itertools.permutations(['-', '+', '*']):
        value = calculator(copy.deepcopy(expression_list), list(order))
        answer = value if answer < value else answer
        
    return answer
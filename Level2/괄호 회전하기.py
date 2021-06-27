from collections import deque

OPENBRACKET  = ('(', '{', '[')
CLOSEBRACKET = (')', '}', ']')

def is_pair(left, right):
    for lb, rb in zip(OPENBRACKET, CLOSEBRACKET):
        if left == lb and right == rb:
            return True
    return False


def is_good(brackets):
    stack = []
    for bracket in brackets:
        if bracket in OPENBRACKET:
            stack.append(bracket)
        else:
            if not stack:
                return False
            top = stack.pop()
            if not is_pair(top, bracket):
                return False
    if stack:
        return False
    return True
            

def solution(brackets):
    brackets = deque(list(brackets))
    length = len(brackets)
    result = 0
    for _ in range(length):
        brackets.append(brackets.popleft())
        copied = brackets.copy()
        if is_good(copied):
            result += 1
    return result
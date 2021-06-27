def get_balance_index(brackets):
    lnum, rnum = 0, 0
    for index, value in enumerate(brackets):
        if value == '(':
            lnum += 1
        elif value == ')':
            rnum += 1
        if lnum == rnum:
            return index + 1

def is_correct_bracket(brackets):
    if brackets[0] == ')' or brackets[-1] == '(':
        return False
    
    st = []
    for bracket in brackets:
        if st and st[-1] != bracket:
            st.pop()
        else:
            st.append(bracket)
    return st == []

def reverse_bracket(brackets):
    return ''.join(['(' if x == ')' else ')' for x in brackets[1:-1]])

def solution(brackets):
    if brackets == '':
        return brackets
    
    pos = get_balance_index(brackets)
    u, v = brackets[:pos], brackets[pos:]
    print(u, v)
    if is_correct_bracket(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + reverse_bracket(u)
before = None

def solution(arr):
    def check(val):
        global before
        if not before == val:
            before = val
            return True
        return False
    return [val for val in arr if check(val)]
def solution(arr):
    '''
    Args:
        arr: List[Int]
        * always len(arr) >= 1
    Returns:
        List[Int]: arr after remove min value
    '''
    arr.remove(min(arr))
    return arr if arr else [-1]
def solution(array, commands):
    '''
    Args
        array: List[int]: numbers
        commands: List[List[int]]
        * command: [i, j, k]: slice i-1 to j, sort, select k
    Returns:
        list: list of selected k
    '''
    return [sorted(array[i-1:j])[k-1] for i, j, k in commands]
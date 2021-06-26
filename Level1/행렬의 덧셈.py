def solution(arr1, arr2):
    return [[x+y for x, y in zip(row1, row2)] for row1, row2 in zip(arr1, arr2)]
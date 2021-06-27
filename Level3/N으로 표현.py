def solution(N, number):
    case_of = [None] + [{N * int('1' * i)} for i in range(1, 9)]

    for level in range(1, 9):
        
        for low in range(1, level):
            other = level - low

            for (x, y) in [(a, b) for a in case_of[low] for b in case_of[other]]:
                case_of[level].add(x + y)
                case_of[level].add(x - y)
                case_of[level].add(x / y)
                case_of[level].add(x * y)
        
        case_of[level] -= {0}

        if number in case_of[level]:
            return level
    return -1
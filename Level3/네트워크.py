def solution(computers, is_connected):

    def visit(computer):
        stack = [computer]

        while stack:
            current = stack.pop()
            is_visited[current] = True
            for other in range(computers):
                if is_connected[current][other] and not is_visited[other]:
                    stack.append(other)            

    count_network = 0
    is_visited = [False] * computers

    for computer in range(computers):
        if not is_visited[computer]:
            visit(computer)
            count_network += 1

    return count_network
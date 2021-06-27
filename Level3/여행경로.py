from collections import defaultdict, deque

def solution(tickets):
    # 이름 오름차순 정렬
    tickets.sort()
    
    # 그래프 초기화
    graph = defaultdict(deque)
    for departure, arrival in tickets:
        graph[departure].append(arrival)
        
    # 스택 초기화
    stack = ['ICN']
    # 경로 초기화
    path = []
    while stack:
        top = stack[-1]
        # 갈 수 있는 항공권이 있다면 스택에 추가
        if graph[top]:
            stack.append(graph[top].popleft())
        # 없으면 경로상에 추가
        else:
            path.append(stack.pop())
    # 역순으로 반환
    return path[::-1]
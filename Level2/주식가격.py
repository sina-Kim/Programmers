def solution(prices):
    result = [0 for _ in prices]
    stack  = []
    
    for index, price in enumerate(prices):
        # 스택에 인덱스가 존재하고, 마지막 원소의 가격이 감소했다면 
        while stack and prices[stack[-1]] > price:
            # 스택에서 꺼내고 결과에 추가
            top = stack.pop()
            result[top] = index-top
        stack.append(index)
    
    # 스택에 원소가 남아있다면
    # 모두 꺼내서 결과에 추가
    while stack:
        top = stack.pop()
        result[top] = len(prices) - top - 1 
    
    return result
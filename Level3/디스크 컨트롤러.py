import heapq

    
def solution(jobs):
    # 요청시간-수행시간 기준 정렬
    # reverse? pop(0) 대신 pop()을 수행하기 위해
    length = len(jobs)
    jobs.sort(reverse=True)
    run_times = []  # 수행 시간 heapq
    current = 0     # 현재 시점
    total_end_time = 0
    
    while jobs:
        # run_times이 비었다면?
        if not run_times:
            start, run_time = jobs.pop()
            current = start if current < start else current 
            heapq.heappush(run_times, (run_time, start))
        
        # current 이전에 요청된 작업을 run_times에 추가
        # max heap을 위해 부호 변경
        while jobs and jobs[-1][0] <= current:
            start, run_time = jobs.pop()
            heapq.heappush(run_times, (run_time, start))
            
        # 가장 긴 작업을 꺼내서 수행
        run_time, start = heapq.heappop(run_times)
        current += run_time
        total_end_time += (current - start)
    
    # 남은 작업들에 대해 처리
    while run_times:
        run_time, start = heapq.heappop(run_times)
        current += run_time
        total_end_time += (current - start)
        
    return total_end_time // length
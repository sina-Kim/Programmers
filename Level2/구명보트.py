def solution(people, limit):
    people.sort()
    
    #  big, small은 구해야 하는 사람의 index이다.
    #  반대로 말하면 아직 구하지 않은 사람의 index이다.
    big   = len(people) - 1
    small = 0
    count = 0
    while big >= small:
        remain_amount = limit
        while big >= small and remain_amount >= people[big]:
            remain_amount -= people[big]
            big -= 1
        
        while big >= small and remain_amount >= people[small]:
            remain_amount -= people[small]
            small += 1
        
        count += 1
    return count
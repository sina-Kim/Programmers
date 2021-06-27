def solution(priorities, location):
    benchmark = priorities[location]
    bigger_list = [ idx for idx in priorities if idx > benchmark]

    if not bigger_list:
        return sum(map(lambda x : x == benchmark, priorities[:location+1]))

    smallest_in_bigger_list = min(bigger_list)
    location_smallest = len(priorities) -1 - priorities[::-1].index(smallest_in_bigger_list)

    if location < location_smallest:
        return sum(map(lambda x : x == benchmark, priorities[location_smallest:])) + sum(map(lambda x : x == benchmark, priorities[:location+1])) + len(bigger_list) + 1
    else:
        return sum(map(lambda x : x == benchmark, priorities[location_smallest:location+1])) + len(bigger_list)
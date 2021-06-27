def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        skill_tree = ''.join(filter(lambda x : x in skill, skill_tree))
        for l, r in zip(skill, skill_tree):
            if not l == r:
                break
        else:
            answer += 1
    return answer
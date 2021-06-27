from collections import defaultdict
from random import randint
import sys
sys.setrecursionlimit(10**6)

def solution(weights, edges):
    
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        
    total = sum(weights)
    ans = 0
    if not total == 0:
        return -1
    a = 1
    def dfs(current, parent):
        ans = 0        
        for other in graph[current]:
            if other == parent:
                continue
            ans += dfs(other, current)
        
        if not parent == -1:
            weight, weights[current] = weights[current], 0
            ans += abs(weight)
            weights[parent] += weight
            
        return ans
    
    return dfs(randint(0, len(weights)-1), -1)
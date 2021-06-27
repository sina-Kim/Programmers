from heapq import heappush, heappop, heapify
from enum import Enum

class StrEnum(str, Enum):
    def __repr__(self):
        return self.value
    def __str__(self):
        return self.value
    
class Command(StrEnum):
    insert = 'I'
    delete = 'D'
    
def solution(operations):
    maxheap = []
    minheap = []
    field_types = (str, int)
    
    for operation in operations:
        command, digit = [fy(val) for fy, val in
                          zip(field_types, operation.split(' '))]
        
        if command == Command.insert:
            heappush(minheap, digit)
            heappush(maxheap, -digit)
        
        elif command == Command.delete:
            if not maxheap:  continue
            
            if digit == 1:
                maxval = heappop(maxheap)
                minheap.remove(-maxval)
                heapify(minheap)
            elif digit == -1:
                minval = heappop(minheap)
                maxheap.remove(-minval)
                heapify(maxheap)
                
    if not maxheap:
        return [0, 0]
    return [-maxheap[0], minheap[0]]
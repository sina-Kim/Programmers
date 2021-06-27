def solution(bridge_length, weight, truck_weights):
    blank  = 0
    bridge = [blank for _ in range(bridge_length)]
    truck_on_bridge = blank
    
    time = 0
    
    while len(truck_weights):
        in_truck  = truck_weights[0]
        out_truck = bridge[0]
        
        if truck_on_bridge + in_truck - out_truck <= weight:
            truck_on_bridge += (in_truck - out_truck)
            bridge.pop(0)
            bridge.append(truck_weights.pop(0))
            time += 1
        else:
            truck_on_bridge -= out_truck
            bridge.pop(0)
            bridge.append(blank)
            time += 1
    
    time += bridge_length
    return time
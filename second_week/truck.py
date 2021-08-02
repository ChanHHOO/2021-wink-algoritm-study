def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_queue = []
    
    while(truck_weights != []):
        
        for i in range(bridge_length):
            
            if truck_weights != [] and sum(bridge_queue) + truck_weights[0] <= weight:
                bridge_queue.append(truck_weights.pop(0))
            answer += 1
        
        bridge_queue.pop(0)
    return answer + len(bridge_queue)

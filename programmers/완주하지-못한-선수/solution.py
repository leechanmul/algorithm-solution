def solution(participant, completion):
    
    p_dict = {}
    answer = ""
    
    for person in participant:
        if person in p_dict:
            p_dict[person] += 1
        else:
            p_dict[person] = 1
    
    for person in completion:
        if person in p_dict:
            p_dict[person] -= 1
            
    for key in p_dict:
        if p_dict[key] == 1:
            answer = key

    return answer

# solution(["leo", "kiki", "eden"], ["eden", "kiki"])
# solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])
# solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])

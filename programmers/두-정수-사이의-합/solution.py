def solution(a, b):
    
    if a == b:
        return a
    
    if a < b:
        min = a
        max = b
        
    if a > b:
        min = b
        max = a
       
    answer = 0
    
    for i in range(min, max+1):
        answer += i
    
    return answer

# solution(3, 5)
# solution(3, 3)
# solution(5, 3)
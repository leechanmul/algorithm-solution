### 📝 문제
https://programmers.co.kr/learn/courses/30/lessons/42576

### 🌱 내 풀이
```python
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
```

### 🔥 풀이 과정
처음엔 `set`을 사용하여 차집합으로 해결할 생각이었는데, 동명이인인 경우 전부 제거해버려서 사용할 수 없었다.
그래서 `dictionary`를 이용해 `선수 이름`을 `key`로 잡아 참가자 목록에서 `이름이 반복된 수`를 `value`로 넣었고, 완주자 목록을 반복할 때 `value`를 하나씩 제거하는 방법을 선택했다.

### 🤕 공부할 점
아직 `Pythonic`한 코드를 작성하지 못해서 코드가 구구절절 길어지는 문제가 있다.
```python
if person in p_dict:
	p_dict[person] += 1
else:
	p_dict[person] = 1
```
이 부분도
```python
if person in p_dict:
	p_dict.get(person, 0) + 1
```
`get`을 사용해 줄일 수 있고, 밑에 두 개의 반복문도 한 번에 처리할 수 있다.
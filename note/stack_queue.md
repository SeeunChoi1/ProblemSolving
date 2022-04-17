# Stack / Queue

스택과 큐는 다음 두 핵심 함수로 이루어짐
* 삽입 push
* 삭제 pop
> 오버플로 : 수용할 수 있는 크기를 넘어선 상태에서 삽입  
> 언더플로 : 데이터가 없는 상태에서 삭제  

## 스택 Stack
후입선출  
* append : 가장 뒤쪽에 데이터 삽입
* pop : 가장 뒤쪽에서 데이터를 꺼냄
```python
stack = []
# 삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력
```

## 큐 Queue
선입선출  
deque 객체를 리스트 자료형으로 변경하려면 list() 메서드 이용
```python
from collections import deque
# 큐 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 다음 출력을 위해 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력
```

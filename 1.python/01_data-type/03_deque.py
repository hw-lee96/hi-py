# 양방향 큐
## 파이썬의 collections 모듈에서 제공하는 자료구조로 양쪽 끝에서 효율적인 삽입과 삭제가 가능
from collections import deque

dq = deque()
dq.append('a')
dq.append('b')
dq.append('c')
print(dq) # 출력 결과 : deque(['a', 'b', 'c'])

dq.appendleft('x') # 맨 앞에 추가
print(dq) # 출력 결과 : deque(['x', 'a', 'b', 'c'])
value = dq.pop() # 맨 뒤 제거
print(dq) # 출력 결과 : deque(['x', 'a', 'b'])
value = dq.popleft() # 맨 앞 제거
print(dq) # 출력 결과 : deque(['a', 'b'])
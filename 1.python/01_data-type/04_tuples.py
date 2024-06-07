# 시퀀스(Sequence) 타입
# 값이 연속적으로 나열된 자료형
# 파이썬에서 사용하는 자료형 중 하나로, 여러 개의 값을 하나의 데이터 구조로 묶어서 관리할 수 있는 불변 시퀀스
# list와 유사하지만 한 벙 생성되면 각 요소의 값을 수정 / 삭제할 수 없다.
# 주로 데이터의 집합을 안전하게 유지하거나, 함수에서 여러 값을 반환할 때 사용

## str : 문자열 값을 가지는 자료형
## list : 여러 값을 담을 수 있는 가변형 자료형
## tuple : 여러 값을 담을 수 있는 불변형 자료형
name = 'ohgiraffers'
print(type(name)) # 출력 결과 : <class 'str'>
list = [0,1,2,3]
print(type(list)) # 출력 결과 : <class 'list'>
tuple = (0,1,2,3)
print(type(tuple)) # 출력 결과 : <class 'tuple'>

safari_tupe = ('Bear', 'Koara', 'Gorilla', 'pig')
print(safari_tupe) # 출력 결과 : ('Bear', 'Koara', 'Gorilla', 'pig')

# 중첩으로 표현 가능
tuples = (1,2,'hello'), ('test',1,2,3,4)
print(tuples) # 출력 결과 : ((1, 2, 'hello'), ('test', 1, 2, 3, 4))
print(tuples[0]) # 출력 결과 : (1, 2, 'hello')
print(tuples[0][0]) # 출력 결과 : 1

# tuple 연산
## 불변 객체이므로 요소 값을 한 번 할당하면 추가 / 수정 / 삭제가 불가
# tuples[0] = (1,2,3,4) # error
testList = (1,2,3,4)
print(id(testList)) # 출력 결과 : 1923124902736 (주소값을 반환)
testList = (3,4,5)
print(id(testList)) # 출력 결과 : 2490207883712 (새로운 tuple이 생성됨. 에러는 발생하지 않음)
# 파이썬은 선언과 할당이 동시에 이뤄지므로, 둘은 아예 다른 별도의 변수임

# 튜플 간 연산
another_safari_tuple = ('monkey', 'tiger', 'wolf')
print(safari_tupe + another_safari_tuple) # 출력 결과 : ('Bear', 'Koara', 'Gorilla', 'pig', 'monkey', 'tiger', 'wolf')
print(safari_tupe * 3) # 출력 결과 : ('Bear', 'Koara', 'Gorilla', 'pig', 'Bear', 'Koara', 'Gorilla', 'pig', 'Bear', 'Koara', 'Gorilla', 'pig')
print(len(safari_tupe + another_safari_tuple)) # 7



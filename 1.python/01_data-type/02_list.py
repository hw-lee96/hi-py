# List
# 일련의 값이 모인 집합을 다루기 위한 자료형
# 일반적인 프로그래밍 언어와 다르게 길이를 동적으로 조절할 수 있어 list 라고 부른다.

fruits = ['orange', 'apple', 'pear', 'kiwi', 'apple']
print(fruits) # 출력 결과 : ['orange', 'apple', 'pear', 'kiwi', 'apple']
print(fruits[0]) # 출력 결과 : orange

# List 유용한 메소드
## 1. count() : 특정 인자의 개수 확인. 전체 수는 안됨
print('apple : ', fruits.count('apple')) # 출력 결과 : 2
print('watermelon : ', fruits.count('watermelon')) # 출력 결과 : 0

## 2. index() : 특정 인자의 인덱스 값 확인. 같은 값이 여러개인 경우 가장 처음 탐색된 인덱스를 반환
print('index : ',  fruits.index('apple')) # 출력 결과 : 1
# print('index : ',  fruits.index('watermelon')) # 출력 결과 : error
## 인덱스 3이후부터 탐색하라는 의미
print('index : ', fruits.index('apple', 3)) # 출력 결과 : 4

## 3. reverse() : list 를 역으로 정렬하며, 원본 배열에 영향을 줌
fruits.reverse()
print(fruits) # 출력 결과 : ['apple', 'kiwi', 'pear', 'apple', 'orange']

## 4. append() : list 끝에 값을 추가
fruits.append('pineapple')
print(fruits) # 출력 결과 : ['apple', 'kiwi', 'pear', 'apple', 'orange', 'pineapple']

## 5. sort() : 요소를 정렬. 원본 배열에 영향을 줌
fruits.sort() # 기본적으로는 오름차순 정렬
print(fruits) # 출력 결과 : ['apple', 'apple', 'kiwi', 'orange', 'pear', 'pineapple']
fruits.sort(reverse=True) # 내림차순 정렬
print(fruits) # 출력 결과 : ['pineapple', 'pear', 'orange', 'kiwi', 'apple', 'apple']
fruits.sort(key=len) # 길이 오름차순
print(fruits) # 출력 결과 : ['pear', 'kiwi', 'apple', 'apple', 'orange', 'pineapple']
fruits.sort(key=len, reverse=True) # 길이 내림차순
print(fruits) # 출력 결과 : ['pineapple', 'orange', 'apple', 'apple', 'pear', 'kiwi']

# del 키워드 : 원본 배열의 일부 혹은 전체를 제거
abclist = ['A', 'B', 'C', 'D', 'E', 'F']
print(abclist) # 출력 결과 : ['A', 'B', 'C', 'D', 'E', 'F']
del abclist[0] # 0번 인덱스의 값을 제거
print(abclist) # 출력 결과 : ['B', 'C', 'D', 'E', 'F']
del abclist[1:3] # 1부터 3이전까지 제거
print(abclist) # 출력 결과 : ['B', 'E', 'F'] (위에서 원본 배열이 영향 받아서 출력 값이 이렇게 됨)
del abclist # 배열을 삭제
# print(abclist) # 출력 결과 : error
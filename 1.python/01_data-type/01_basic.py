# 기본 자료형

# 1. 숫자형
# int : 정수 값을 가지는 자료형
# float : 소수 값을 가지는 자료형

num1 = 1
num2 = 3.14

print(type(num1)) # 출력 결과 : <class 'int'>
print(type(num2)) # 출력 결과 : <class 'float'>

# 연산
num3 = 11
num4 = 7
print(num3 + num4) # 출력 결과 : 18
print(num3 - num4) # 출력 결과 : 4
print(num3 * num4) # 출력 결과 : 77
print(num3 / num4) # 출력 결과 : 1.5714285714285714
print(num3 % num4) # 출력 결과 : 4

# 몫(정수 값)만 구하는 연산
print(num3 // num4) # 출력 결과 : 1

# 제곱 연산
base = 9
exponent = 2
print(base ** exponent) # 출력 결과 : 81

# 2 논리형 (Bool)
bool1 = True
bool2 = False

print(type(bool1)) # 출력 결과 : <class 'bool'>
print(type(bool2)) # 출력 결과 : <class 'bool'>

# 3. 문자형 (String) 쌍따옴표("")와 홀따옴표('') 둘 다 사용 가능
fruit = 'apple'
print(fruit) # 출력 결과 : apple

capasity = str(300)
print(type(capasity)) # 출력 결과 : <class 'str'>

print("""
      Long 코트보다 긴 건?
      double 코드
      짧은 건?
      int 패딩
""")

# 문자열은 index를 가지고 있어 인덱싱을 통해 원하는 문자 하나를 추출할 수 있다.
address = '대한민국 서울시 서초구'
print(address[5]) # 출력 결과 : 서
print(address[9]) # 출력 결과 : 서

# slice
# 9번 인덱스부터 끝까지
print(address[9:]) # 출력 결과 : 서초구
#5부터 8이전까지 추출
print(address[5:8]) # 출력 결과 : 서울시
# 1~12까지 4개씩 건너뛰면서 추출
print(address[1:12:4]) # 출력 결과 : 한서서
# 문자열 뒤집기
print(address[::-1]) # 출력 결과 : 구초서 시울서 국민한대
# 뒤의 n번째 인덱스부터 (끝까지)
print(address[-3:]) # 출력 결과 : 서초구

# 문자열 * 연산
subject = 'python'
# 해당 문자열을 n번 반복
print(subject * 3) # 출력 결과 : pythonpythonpython

# 문자열 관련 메소드
# 1. replace() : 문자열 치환 (별도 정규식 없이도 전부 치환 함)
enroll_date = '2024/12/16'
rep_enroll_date = enroll_date.replace("/", "-")
print(rep_enroll_date) # 출력 결과 : 2024-12-16 

# 2. strip() : 특정 문자 집합을 제거
origin = 'ohgiraffers'
with_white_space = '      oh giraffers'

## 2.1. 공백 제거
print(with_white_space) # 출력 결과 : '      oh giraffers'
print(with_white_space.strip()) # 출력 결과 : oh giraffers
print(with_white_space.strip('      o')) # 출력 결과 : h giraffers
print(with_white_space.strip('      os')) # 출력 결과 : h giraffer

# 3. 대소문자 관련 메소드
origin_str = 'hELLO wORLD!'
print(origin_str.upper()) # 출력 결과 : HELLO WORLD!
print(origin_str.lower()) # 출력 결과 : hello world!
# 맨 첫 글자만 대문자로
print(origin_str.capitalize()) # 출력 결과 : Hello world!

# 4. 문자형 포맷
# 변수 포맷을 이용하여 문자열에 변수 값을 삽입
# 편수 포맷 종류
## %s : 문자열
## %c : 문자
## %d : 정수
## %f : 실수

x = 10
print("x is %d" % x) # 출력 결과 : x is 10
print("x is %d is %d" % (x, x)) # 출력 결과 : x is 10 is 10
y = 'code'
print("y is %s" % y) # 출력 결과 : y is code

# 중괄호를 이용해 format에 기입한 변수를 순서대로 기입하게 할 수 있다. 
print("x is {1} y is {0}" .format(y, x)) # 출력 결과 : x is 10 y is code

# 형 변환

## 암시적 형 변환
### 정수와 함께 사용하면 True = 1, False = 0으로 자동 형변환 된다.
print(True + 3) # 출력 결과 : 4
print(3 + 5.0) # 출력 결과 : 8.0
### 문자열과는 암시적으로 불가하여 명시적으로 형 변환을 해주어야 함
# print(3 + '5')

## 명시적 형 변환
print(int('3') + 4) # 출력 결과 : 7
print(float('3')) # 출력 결과 : 3.0
print(str(1)) # 출력 결과 : 1
print(str(1)) # 출력 결과 : 1
print(str(1.0)) # 출력 결과 : 1.0
print(str({1,2,3})) # 출력 결과 : {1, 2, 3}


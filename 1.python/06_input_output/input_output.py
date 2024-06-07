# 입출력
# file open 종류
# 1. r : 읽기
# 2. w : 쓰기
# 3. a = 추가. 파일의 마지막에 새로운 내용을 추가할 때 사용
# 파일을 쓰기 모드로 열면 해당 파일이 이미 존재할 경우 원래 있던 내용이 모두 사라지고 덮어씌워짐
# 해당 파일이 존재하지 않으면 새로운 파일이 생성 됨

# 파일 쓰기
# f = open('newFile.txt', 'w')
# f.close

# 특정 폴더 안에 생성
# f = open('C:/Users/HW/Documents/hi/python/newFile.txt')

# 파일을 쓰기 모드로 열어서 내용 쓰기
# f = open('newFile.txt', 'w')
# for i in range(1, 11):
#     data = f'{i}번째 줄입니다.\n'
#     f.write(data)
# f.close()

# 파일 한 줄 읽기
# f = open('newFile.txt', 'r')
# line = f.readline()
# print(line)
# f.close()

# # 반복문 이용 모든 내용 읽기
# f = open('newFile.txt', 'r')
# while True:
#     line = f.readline()
#     if line == '' : break
#     print(line)
# f.close()

# 모든 줄 읽기
# f = open('newFile.txt', 'r')
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close()

# for 문 자체 사용
# f = open('newFile.txt', 'r')
# for line in f:
#     print(line)
# f.close()

# 파일에 새로운 내용 추가
f = open('newFile.txt', 'a', encoding='utf-8')
for i in range(11, 15):
    data = f'{i}번째 줄입니다.\n'
    f.write(data)
f.close()

# with 문 : 파일을 열면 항상 닫아야 하는데, 이렇게 열고 닫는 것을 자동으로 처리해줌
with open('newFile2.txt', 'w') as f:
    f.write('Life is too short, you need python')
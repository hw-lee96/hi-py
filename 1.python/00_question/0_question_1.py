# ### **문제 2: 학생 성적 관리 프로그램**
# 학생들의 성적을 관리하는 프로그램을 작성하세요. 프로그램은 다음 기능을 포함해야 합니다:

# 1. 학생의 이름과 성적을 입력 받아 저장합니다.
flag = False
sList = []

while(flag == False):
    print('학생 이름을 입력해주세요. 입력을 완료한 경우 x를 입력해주세요.')
    s = input()
    if(s == 'x'):
        break
    else:
        print('학생의 성적을 입력해주세요')
        p = input()
        sList.append([s,int(p)])
print('입력이 완료되었습니다.')

# 2. 특정 학생의 성적을 조회합니다.
print()
print('조회하려는 학생의 이름을 입력해주세요')
s2 = input()
print(s2 + ' 학생의 점수 : %d' % list(filter(lambda x : x[0] == s2, sList))[0][1])

# 3. 모든 학생의 평균 성적을 계산하여 출력합니다.
print()
a = sum(map(lambda x : x[1], sList)) / len(sList)
print('모든 학생 평균 점수 : %d' % a)

# 4. 성적이 특정 점수 이상인 학생들의 이름을 출력합니다.
print()
print('성정이 평균 이하인 학생을 조회합니다.')
print(list(filter(lambda x : x[1] <= a, sList)))


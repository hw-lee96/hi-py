# ### **문제 2: 학생 성적 관리 프로그램**
# 학생들의 성적을 관리하는 프로그램을 작성하세요. 프로그램은 다음 기능을 포함해야 합니다:

# 1. 학생의 이름과 성적을 입력 받아 저장합니다.
# 2. 특정 학생의 성적을 조회합니다.
# 3. 모든 학생의 평균 성적을 계산하여 출력합니다.
# 4. 성적이 특정 점수 이상인 학생들의 이름을 출력합니다.

students = {}
# students = { '이형우1' : 30, '이형우2' : 50, '이형우3' : 70 }

# 1. 학생의 이름과 성적을 입력 받음
def enterGrade():
    print('학생의 이름을 입력해주세요.')
    name = input()
    print('성적을 입력해주세요.')
    grade = input()

    students[name] = int(grade)

# 2. 특정 학생의 성적을 조회
def findGrade():
    print('학생의 이름을 입력해주세요.')
    name = input()

    grade = students.get(name)
    if (grade != None):
        print('%s 학생의 점수는 %d 입니다.' % (name, grade))
    else:
        print('데이터가 존재하지 않습니다.')
    print()

# 3. 모든 학생의 평균 성적 조회
def findAvgGrade():
    grades = list(students.values())
    avgGrade = sum(grades) / len(grades)
    print('학생들의 평균 성적은 %d 입니다.' % avgGrade)
    print()

# 4. 특정 점수 이상인 학생을 조회
def findHigherThenInputGrade():
    print('기준 점수를 입력해주세요.')
    grade = int(input())
    findList = ['%s(%d점)' % (name, grade) for name, grade in filter(lambda x : x[1] >= grade, students.items())]
    print(', '.join(findList))
    
while(True) :
    print('=== 메뉴를 입력 해주세요 ===')
    print('1 : 성적 입력')
    print('2 : 성적 조회')
    print('3 : 전체 평균 조회')
    print('4 : 특정 점수 이상인 학생 조회')

    menu = input()
    match menu:
        case '1':
            enterGrade()
        case '2':
            findGrade()
        case '3':
            findAvgGrade()
        case '4':
            findHigherThenInputGrade()
        case '5':
            break
        case _:
            break

print('종료되었습니다.')

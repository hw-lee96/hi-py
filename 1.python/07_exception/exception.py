# 예외처리
# 예외처리 기본 문법
# try:
# escept:

# try:
#     4 / 0
# except:
#     print('예외 발생')

# try:
#     4 / 0
# except ZeroDivisionError as e:
#     print(e)

# try:
#     a = [1, 2]
#     print(a[3])
#     4 / 0
# except ZeroDivisionError:
#     print('0으로 나눌 수 없습니다.')
# except IndexError:
#     print('인덱싱 할 수 없습니다.')

# # try-finally
# try:
#     f = open('foo.txt', 'w')
# finally:
#     f.close()

# try-else
# try 문 수행 중 오류가 발생하지 않으면 수행
# try:
#     age = int(input('나이를 입력해주세요.\n'))
# except:
#     print('입력이 정확하지 않습니다.')
# else:
#     if age <= 18:
#         print('미성년자는 출입이 불가합니다.')
#     else:
#         print('환영합니다.')

# 오류 회피하기
# try문 안에서 에러가 발생하더라도 pass를 이용해 예외처리되지 않도록 할 수 있다.
# try:
#     f = open('파일 없음', 'r')
# except FileNotFoundError:
#     print('파일이 없습니다. (pass)')
#     pass

# 예외 발생시키기
# 내장 클래스인 Exception 클래스를 상속하여 처리 가능
class MyError(Exception):
    pass

# raise를 이용해 예외를 발생시킬 수 있음
def say_nick(nick):
    if nick == '돼지':
        raise MyError()
    print('돼지는 됨')

try:
    say_nick('곰')
    say_nick('돼지')
except MyError:
    print('다른건 안됨')
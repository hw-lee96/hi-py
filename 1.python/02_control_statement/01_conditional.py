# 조건문
# if 문
# 구문을 중괄호({})로 감싸지 않기 떄문에 tab 을 통해 구문의 구분하게 됨
# if 조건식:
#   실행 내용

x = int(input('정수 하나를 입력 해주세요 : '))
if (x > 0):
    print('입력하신 %d 는 양수입니다.' % x)
elif (x == 0):
    print('입력하신 숫자는 %d입니다.' % x)
else:
    print('입력하신 %d 는 음수입니다.' % x)

# match 문
# 주어진 값을 case 블록의 값과 비교해 일치하는 case를 실행
print('=== vending machine ===')
print('사이다(500) 콜라(600) 환타(700) 밀키스(1000)')
print('원하시는 음료를 선택 해주세요 : ')
drink = input()
price = 0
match drink:
    case'사이다':
        print('사이다를 선택하셨습니다.')
        price = 500
    case'콜라':
        print('콜라를 선택하셨습니다.')
        price = 600
    case'환타':
        print('환타를 선택하셨습니다.')
        price = 700
    case'밀키스':
        print('밀키스를 선택하셨습니다.')
        price = 1000
    case _: # default
        print('제공되는 음료수가 아닙니다.')

print('%d 원을 투입해주세요' % price)
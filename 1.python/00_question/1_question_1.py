### **문제: 은행 관리 프로그램**
# 1. `Account` 클래스를 정의하세요. 이 클래스는 다음과 같은 특징을 가지고 있어야 합니다:
#     - `__init__` 메서드를 사용하여 은행 계좌의 소유주 이름과 초기 잔액을 설정합니다.
#     - `deposit` 메서드를 사용하여 입금을 처리합니다.
#     - `withdraw` 메서드를 사용하여 출금을 처리합니다. 출금할 금액이 잔액보다 크면 출금을 허용하지 않습니다.
#     - `display_balance` 메서드를 사용하여 현재 잔액을 출력합니다.
# 2. `Bank` 클래스를 정의하세요. 이 클래스는 다음과 같은 특징을 가지고 있어야 합니다:
#     - `__init__` 메서드를 사용하여 은행의 이름을 설정합니다.
#     - `create_account` 메서드를 사용하여 새로운 계좌를 생성합니다.
#     - `get_account` 메서드를 사용하여 계좌를 반환합니다.
#     - `display_accounts` 메서드를 사용하여 현재 은행에 있는 모든 계좌 정보를 출력합니다.
# 3. 사용자가 여러 번 계좌를 생성하고 입금, 출금, 잔액 조회 등의 작업을 수행할 수 있도록 하세요. 
# 사용자가 프로그램을 종료하고 싶을 때에는 "종료"를 입력하면 됩니다.

class Account():
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    # 입금
    def deposit(self, amount):
        if (amount > 0):
            self.__balance += int(amount)
        else:
            raise ValueError('입금 금액은 양수여야 합니다.')

    # 출금
    def withdraw(self, amount):
        if (amount > 0):
            self.__balance -= int(amount)
        else:
            raise ValueError('출금 금액은 양수여야 합니다.')
    
    # 잔액 조회
    def display_balance(self):
        return self.__balance
    
class Bank():
    def __init__(self, name):
        self.name = name
        self.account_list = {}

    # 계좌 생성
    def create_account(self):
        print('생성하려는 계좌 번호를 입력해주세요.')
        account_number = input()

        print('이름을 입력해주세요.')
        name = input()

        print('초기 금액을 입력해주세요.')
        amount = input()

        new_account = Account(name, int(amount))
        
        self.account_list[account_number] = new_account

        print('계좌 생성이 완료되었습니다.')

    # 계좌 조회
    def get_account(self, account_number):
        return self.account_list.get(account_number)

    # 전체 계좌번호 조회
    def display_accounts(self):
        return list(self.account_list)        

# 계좌 생성 / 계좌 조회 / 전체 계좌 조회 / 입금 / 출금 / 잔액 조회
bank = Bank('하이원')

while(True):
    print()
    print('=== 원하는 메뉴를 선택해주세요 ===')
    print('1 : 계좌 생성')
    print('2 : 계좌번호 조회')
    print('3 : 전체 계좌 조회')
    print()
    print('4 : 입금')
    print('5 : 출금')
    print('6 : 잔액 확인')
    print()

    menu = input()
    
    try:
        match(menu):
            case '1':
                bank.create_account()
            case '2':
                # 계좌 조회
                print('조회하려는 계좌 번호를 입력해주세요')
                account_number = input()
                account = bank.get_account(account_number)

                if account == None:
                    print()
                    print('### 존재하지 않는 계좌번호입니다.')
                else:
                    print()
                    print('### 입력하신 계좌의 소유주는 [%s]이며, 잔액은 [%d]입니다.' %(account.name, account._Account__balance))

            case '3':
                print('### 전체 계좌번호 목록을 조회합니다')
                print(bank.display_accounts())
            case '4':
                print('입금하려는 계좌번호를 입력해주세요')
                account_number = input()
                account = bank.get_account(account_number)

                if account == None:
                    print()
                    print('### 존재하지 않는 계좌번호입니다.')
                else:
                    print('입금하려는 금액을 입력해주세요')
                    amount = input()
                    account.deposit(int(amount))
                    print()
                    print('### 입금 완료했습니다. 현재 잔액 : [%d]' % account.display_balance())
            case '5':
                print('출금하려는 계좌번호를 입력해주세요')
                account_number = input()
                account = bank.get_account(account_number)

                if account == None:
                    print()
                    print('### 존재하지 않는 계좌번호입니다.')
                else:
                    print('출금하려는 금액을 입력해주세요')
                    amount = input()
                    account.withdraw(int(amount))
                    print()
                    print('### 출금 완료했습니다. 현재 잔액 : [%d]' % account.display_balance())
            case '6':
                print('잔액을 조회할 계좌번호를 입력해주세요')
                account_number = input()
                account = bank.get_account(account_number)

                if account == None:
                    print()
                    print('### 존재하지 않는 계좌번호입니다.')
                else:
                    print()
                    print('### 현재 잔액은 [%d]입니다.' % account.display_balance())
            case _: break
    except ValueError as e:
        print(e)

print('종료 되었습니다.')
'''
함수
'''

# 은행 계좌 개설하기
def open_account():
    print("새로운 계좌를 개설합니다.")

# 입금 처리
def deposit(balance, money):
    print("{0}원을 입금했습니다. 잔액은 {1}원입니다.".format(money, balance + money))
    return balance + money #입금 후 잔액 정보 반환

# 영업 시간 내 출금 처리
def withdraw(balance, money):
    # 잔액이 출금 금액보다 많으면 출금 가능
    if balance >= money:
        print("{0}원을 출금했습니다. 잔액은 {1}원입니다.".format(money, balance - money))
        return balance - money
    # 잔액이 출금 금액보다 적으면 출금 불가
    else:
        print("잔액이 부족합니다. 잔액은 {0}원입니다.".format(balance))
        return balance

# 영업 시간 이후 출금 처리 : 수수료 부과
def withdraw_night(balance, money):
    commission = 100 #출금 수수료
    print("업무 시간 외에 {0}원을 출금했습니다.".format(money))
    return commission, balance - money - commission #인자 2개 return 가능

def main():
    open_account()
    #새로운 계좌를 개설합니다.

    balance = 0 #초기 잔액
    print("입금 전 잔액: {0}".format(balance)) #입금 전 잔액: 0

    balance = deposit(balance, 1000) #1000원 입금
    #1000원을 입금했습니다. 잔액은 1000원입니다.
    print("입금 후 잔액: {0}".format(balance)) #입금 후 잔액: 1000

    commission, balance = withdraw_night(balance, 500)
    #업무 시간 외에 500원을 출금했습니다.
    print("수수료: {0}원, 잔액: {1}원".format(commission, balance)) #수수료: 100원, 잔액: 400원

main()

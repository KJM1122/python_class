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

# 출금 처리
def withdraw(balance, money):
    # 잔액이 출금 금액보다 많으면 출금 가능
    if balance >= money:
        print("{0}원을 출금했습니다. 잔액은 {1}원입니다.".format(money, balance - money))
        return balance - money
    # 잔액이 출금 금액보다 적으면 출금 불가
    else:
        print("잔액이 부족합니다. 잔액은 {0}원입니다.".format(balance))
        return balance

def main():
    open_account()
    #새로운 계좌를 개설합니다.

    balance = 0 #초기 잔액
    print("입금 전 잔액: {0}".format(balance)) #입금 전 잔액: 0

    balance = deposit(balance, 1000) #1000원 입금
    #1000원을 입금했습니다. 잔액은 1000원입니다.
    print("입금 후 잔액: {0}".format(balance)) #입금 후 잔액: 1000

    balance = withdraw(balance, 2000)
    #잔액이 부족합니다. 잔액은 1000원입니다.

    balance = withdraw(balance, 500)
    #500원을 출금했습니다. 잔액은 500원입니다.
    print("출금 후 잔액: {0}".format(balance)) #출금 후 잔액: 500

main()

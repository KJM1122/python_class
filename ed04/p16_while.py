'''
while문
'''

def main():
    customer = '토르'
    person = None

    while customer != person:
        print('{0}님, 음료가 준비됐습니다.'.format(customer))
        person = input('이름이 어떻게 되세요?')
    print("맛있게 드세요!")

    # 토르님, 음료가 준비됐습니다.
    # 이름이 어떻게 되세요?정민
    # 토르님, 음료가 준비됐습니다.
    # 이름이 어떻게 되세요?토르
    # 맛있게 드세요!

main()

'''
for문
'''

def main():
    orders = ['아이언맨', '토르', '스파이더맨']
    for customer in orders:
        print('{0}님, 음료 나왔습니다.'.format(customer))

    # 아이언맨님, 음료 나왔습니다.
    # 토르님, 음료 나왔습니다.
    # 스파이더맨님, 음료 나왔습니다.


main()

'''
for문
'''

def main():
    for wating_no in [1, 2, 3, 4, 5]:
        print('대기번호:{}'.format(wating_no))
        # 대기번호:1
        # 대기번호:2
        # 대기번호:3
        # 대기번호:4
        # 대기번호:5

    print('-' * 50)

    for wating_no in range(5): #0<=x<5
        print('대기번호:{}'.format(wating_no))
        # 대기번호:0
        # 대기번호:1
        # 대기번호:2
        # 대기번호:3
        # 대기번호:4

    print('-' * 50)

    for wating_no in range(1, 6): #1<=x<6
        print('대기번호:{}'.format(wating_no))
        # 대기번호:1
        # 대기번호:2
        # 대기번호:3
        # 대기번호:4
        # 대기번호:5

    print('-' * 50)

    for wating_no in range(1, 6, 2): #1<=x<6 2간격으로
        print('대기번호:{}'.format(wating_no))
        # 대기번호:1
        # 대기번호:3
        # 대기번호:5


main()

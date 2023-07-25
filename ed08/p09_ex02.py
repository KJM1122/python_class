'''
문제
'''


def save_battery(level):
    if 30 < level <= 100:
        print("일반 모드")
    elif 5 < level <= 30:
        print("절전 모드")
    else:
        raise Exception('종료')


def main():
    level = int(input("배터리 잔량? "))
    try:
        save_battery(level)
    except Exception as err:
        print('Exception:', err)


main()

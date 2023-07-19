'''
input
'''


def main():
    answer = input('아무 값이나 입력하세요 > ')
    print("입력한 값은 '{}'입니다.".format(answer))
    print(type(answer))  # 기본 type은 문자열(str)
    print(type(int(answer)))

    # 아무 값이나 입력하세요 > 1
    # 입력한 값은 '1'입니다.
    # <class 'str'>
    # <class 'int'>


main()

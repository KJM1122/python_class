'''
계산기 프로그램
'''


def main():
    print('나누기 전용 계산기')
    try:
        num1 = int(input('첫 번째 숫자를 입력하세요.> '))
        num2 = int(input('두 번째 숫자를 입력하세요.> '))

        print('{0}/{1} = {2}'.format(num1, num2, int(num1 / num2)))
        # ValueError: invalid literal for int() with base 10: '삼'

    except ValueError:
        print('숫자를 입력해주세요.')


main()

# 나누기 전용 계산기
# 첫 번째 숫자를 입력하세요.> 6
# 두 번째 숫자를 입력하세요.> 3
# 6/3 = 2

# 첫 번째 숫자를 입력하세요.> 6
# 두 번째 숫자를 입력하세요.> 삼
# 숫자를 입력해주세요.

'''
계산기 프로그램
'''


def main():
    print('나누기 전용 계산기')
    try:
        num1 = int(input('첫 번째 숫자를 입력하세요.> '))
        num2 = int(input('두 번째 숫자를 입력하세요.> '))

        print('{0}/{1} = {2}'.format(num1, num2, int(num1 / num2)))

    except ValueError:
        print('숫자를 입력해주세요.')
    except ZeroDivisionError as err:
        print('ZeroDivisionError:', err)
    finally:
        print('계산기를 사용해주셔서 감사합니다.')

    print('프로그램 종료!')  # 예외가 발생하면 프로그램이 끝까지 내려오지 않아 출력 안 됨


main()

# 나누기 전용 계산기
# 첫 번째 숫자를 입력하세요.> 6
# 두 번째 숫자를 입력하세요.> 3
# 6/3 = 2
# 계산기를 사용해주셔서 감사합니다.
# 프로그램 종료!

# 나누기 전용 계산기
# 첫 번째 숫자를 입력하세요.> 6
# 두 번째 숫자를 입력하세요.> 0
# ZeroDivisionError: division by zero
# 계산기를 사용해주셔서 감사합니다.
# 프로그램 종료!

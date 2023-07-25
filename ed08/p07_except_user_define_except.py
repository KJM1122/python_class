'''
계산기 프로그램
'''


class BigNumberError(Exception):  # 사용자 정의 예외, Exception 상속
    def __init__(self, msg):  # 스페셜 메서드, 던더 메서드(dunder method)
        self.msg = msg

    def __str__(self):
        return '[오류 코드: 001] ' + self.msg  # 자바에서 toString(), 메시지 가공


def main():
    print('나누기 전용 계산기')
    try:
        num1 = int(input('첫 번째 숫자를 입력하세요.> '))
        num2 = int(input('두 번째 숫자를 입력하세요.> '))

        if num1 >= 10 or num2 >= 10:  # 입력받은 숫자가 2자리이면
            raise BigNumberError("입력값: {0}, {1}".format(num1, num2))  # 예외 발생

        print('{0}/{1} = {2}'.format(num1, num2, int(num1 / num2)))

    except ValueError as err:
        print('잘못된 값을 입력했습니다.', err)
    except ZeroDivisionError as err:
        print('ZeroDivisionError:', err)
    except BigNumberError as err:
        print('BigNumberError:', err)
    finally:
        print('계산기를 사용해주셔서 감사합니다.')

    print('프로그램 종료!')


main()

# 나누기 전용 계산기
# 첫 번째 숫자를 입력하세요.> 10
# 두 번째 숫자를 입력하세요.> 5
# BigNumberError: 입력값: 10, 5
# 계산기를 사용해주셔서 감사합니다.
# 프로그램 종료!

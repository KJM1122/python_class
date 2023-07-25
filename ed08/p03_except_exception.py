'''
계산기 프로그램
'''


def main():
    print('나누기 전용 계산기')
    try:
        nums = []
        nums.append(int(input('첫 번째 숫자를 입력하세요.> ')))
        nums.append(int(input('두 번째 숫자를 입력하세요.> ')))
        # nums.append(int(nums[0] / nums[1]))

        print('{0}/{1} = {2}'.format(nums[0], nums[1], nums[2]))
        # IndexError: list index out of range

    except ValueError:
        print('숫자를 입력해주세요.')
    except ZeroDivisionError as err:
        print('ZeroDivisionError:', err)
    except Exception as err:
        print(err)  # list index out of range

    print('프로그램 종료!')  # 예외가 발생하면 프로그램이 끝까지 내려오지 않아 출력 안 됨


main()

# 나누기 전용 계산기
# 첫 번째 숫자를 입력하세요.> 6
# 두 번째 숫자를 입력하세요.> 3
# list index out of range
# 프로그램 종료!

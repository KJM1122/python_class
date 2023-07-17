'''
input()
연산자 간소화
'''

def main():
    temp = int(input('오늘 기온은 어때?')) #정수형으로 입력

    print(temp, type(temp))

    # 연산자 간소화
    if temp >= 30:
        print('너무 더워. 외출 자제')
    elif temp >= 10:
        print('활동하기 좋은 날씨')
    elif temp >= 0:
        print('외투 챙겨.')
    else:
        print('너무 추워. 외출 금지')
    # 오늘 기온은 어때?12
    # 12 <class 'int'>
    # 활동하기 좋은 날씨


main()

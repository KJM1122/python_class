'''
input()
논리 연산자 사용 제어문
'''

def main():
    temp = int(input('오늘 기온은 어때?')) #정수형으로 입력

    print(temp, type(temp))
    # 오늘 기온은 어때?24
    # 24 <class 'int'>

    # 논리 연산자 사용 제어문
    if temp >= 30:
        print('너무 더워. 외출 자제')
    elif 10 <= temp and temp < 30:
        print('활동하기 좋은 날씨')
    elif 0 <= temp and temp < 10:
        print('외투 챙겨.')
    else:
        print('너무 추워. 외출 금지')
    # 오늘 기온은 어때?24
    # 24 <class 'int'>
    # 활동하기 좋은 날씨


main()

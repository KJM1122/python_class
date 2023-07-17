'''
input()
'''

def main():
    weather = input("오늘 날씨는 어때?")

    if weather == '비' or weather == '눈':
        print('우산을 준비하세요!')
    elif weather == '미세먼지':
        print('마스크를 준비하세요!')
    else:
        print('준비물이 필요없어요!')

    print(weather, type(weather))
    # 오늘 날씨는 어때?99
    # 준비물이 필요없어요!
    # 99 <class 'str'>

main()

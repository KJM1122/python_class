'''
지역 변수, 전역 변수
'''

glasses_value = 10  # 전체 3D안경 개수


def rent(glasses, people):  # 3D 안경을 대여한 관객 수
    glasses = glasses - people  # 잔여 안경 개수 = 전체 개수 - 대여한 개수
    print('[함수내부] 남은 3D안경 개수: {0}'.format(glasses))
    return glasses


def main():
    print("전체 3D안경 개수: {}개".format(glasses_value))
    glasses = rent(glasses_value, 2)  # 3D안경을 관객 2명에게 대여
    print("남은 3D안경 개수: {}개".format(glasses))

    # 전체 3D안경 개수: 10개
    # [함수내부] 남은 3D안경 개수: 8
    # 남은 3D안경 개수: 8개


main()

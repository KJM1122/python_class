'''
지역 변수, 전역 변수
'''

# glasses: 전역 변수
glasses = 10  # 전체 3D안경 개수


def rent(people):  # 3D 안경을 대여한 관객 수
    # 그냥 glasses: 지역 변수
    global glasses  # 전역 변수 사용
    glasses = glasses - people  # 잔여 안경 개수 = 전체 개수 - 대여한 개수
    print('[함수내부] 남은 3D안경 개수: {0}'.format(glasses))


def main():
    print("전체 3D안경 개수: {}개".format(glasses))  # 전역 변수 호출
    rent(2)  # 3D안경을 관객 2명에게 대여
    print("남은 3D안경 개수: {}개".format(glasses))

    # 전체 3D안경 개수: 10개
    # [함수내부] 남은 3D안경 개수: 8
    # 남은 3D안경 개수: 8개

    # 전역 변수를 안 쓰는 경우
    # 전체 3D안경 개수: 10개
    # [함수내부] 남은 3D안경 개수: -2
    # 남은 3D안경 개수: 10개


main()
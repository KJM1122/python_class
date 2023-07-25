'''
패키지
'''

from travel_temp import vietnam  # from 패키지 import 모듈


def main():
    # 모듈.클래스().함수()
    trip_to = vietnam.VietnamPackage()  # 인스턴스 생성
    trip_to.detail()  # [베트남 3박 5일 패키지] 다낭 효도 여행 60만원


main()

'''
모듈 공개 설정
'''

from travel_temp import *


def main():
    # Unresolved reference 'vietnam' 오류 -> __init__.py 수정
    trip_to = vietnam.VietnamPackage()
    trip_to.detail()  # [베트남 3박 5일 패키지] 다낭 효도 여행 60만원
    thailand.ThailandPackage().detail()  # [태국 3박 5일 패키지] 방콕, 파타야 여행 50만원


main()

# __name__: travel_temp.thailand
# 이 문장은 외부에서 모듈 실행 시 출력
# [베트남 3박 5일 패키지] 다낭 효도 여행 60만원
# [태국 3박 5일 패키지] 방콕, 파타야 여행 50만원

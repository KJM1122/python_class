'''
모듈 사용하기
'''

import theater_module as tm  # 모듈 Alias로 가져오기 (모듈 이름 간략히 표현)


def main():
    tm.price(3)  # 일반 3명
    tm.price_morning(4)  # 조조 4명
    tm.price_soldier(5)  # 군인 5명

    # 3명, 티켓 가격은 총 45000원입니다.
    # 4명, 티켓 가격은 총 36000원입니다.
    # 5명, 티켓 가격은 총 500원입니다.


main()

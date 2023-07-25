'''
모듈 사용하기
'''

from theater_module import price, price_morning, price_soldier as ps  # price_soldier에 Alias 부여


def main():
    price(3)  # 일반 3명
    price_morning(4)  # 조조 4명
    ps(5)  # 군인 5명

    # 3명, 티켓 가격은 총 45000원입니다.
    # 4명, 티켓 가격은 총 36000원입니다.
    # 5명, 티켓 가격은 총 500원입니다.


main()

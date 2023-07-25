'''
문제
'''


class SoldOutError(Exception):
    def __init__(self):
        pass


def main():
    chicken = 10  # 남은 치킨 수
    waiting = 1  # 대기번호, 1부터 시작

    try:
        while True:
            print("[남은 치킨 : {0}]".format(chicken))
            order = int(input("치킨을 몇 마리 주문하시겠습니까? "))
            if order > chicken:  # 남은 치킨보다 주문량이 많을 때
                print("재료가 부족합니다.")
            else:
                print("[대기번호 {0}] {1}마리를 주문했습니다.".format(waiting, order))
                waiting += 1  # 대기번호 1 증가
                chicken -= order  # 주문 수만큼 남은 치킨 감소

            if order < 1:
                raise ValueError

            if chicken <= 0:
                raise SoldOutError

    except ValueError:
        print("값을 잘못 입력했습니다.")
    except SoldOutError:
        print("재료가 소진돼 더 이상 주문을 받지 않습니다.")
    finally:
        pass


main()

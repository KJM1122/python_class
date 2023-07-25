'''
strftime()
'''
import time
import datetime


def main():
    print(time.strftime('%Y-%m-%d %H:%M:%S'))  # 연-월-일 시:분:초
    # 2023-07-25 10:38:20

    # 오늘 날짜 출력
    print(datetime.date.today())
    # 2023-07-25

    # 두 날짜 사이의 차이를 계산하는 함수: timedelta()
    today = datetime.date.today()
    td = datetime.timedelta(days=100)  # 오늘로부터 100일째 날짜
    print('우리가 만난 지 100일째 되는 날은', today + td)


main()

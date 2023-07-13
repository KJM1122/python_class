'''
random 모듈
'''
from random import * #(random 모듈의 모든 기능 사용)

def main():
    print(random()) #0<=x<1 실수
    print(random())
    print(random())

    print("-" * 50)

    print(random() * 10) #0<=x<10 실수
    print(int(random() * 10)) #0<=x<10 정수
    print(int(random() * 10) + 1) #1<=x<11 정수
    print(int(random() * 45) + 1) #1<=x<46 정수

    print("-" * 50)

    print(randrange(1, 46)) #1<=x<46 정수
    print(randint(1, 45)) #1<=x<=45 정수


main()
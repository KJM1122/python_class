'''
리스트 문제
'''

from random import *

def main():
    num_list = list(range(1, 21)) #1<=x<21
    print(num_list)

    shuffle(num_list)
    print(num_list)

    chicken = num_list.pop()
    coffee = sample(num_list, 3)

    print('-- 당첨자 발표 --')
    print("치킨 당첨자 : {}".format(chicken)) #치킨 당첨자 : 9
    print("커피 당첨자 : {}".format(coffee)) #커피 당첨자 : [1, 3, 6]
    print('-- 축하합니다! --')

    print('-' * 50)

    person = range(1, 21) #1<=x<21
    person = list(person) #list로 변환
    print(person)

    shuffle(person)
    print(person)

    select_data = sample(person, 4) #4명 중복 없이 추출
    print(select_data)

    print('-- 당첨자 발표 --')
    print("치킨 당첨자 : {}".format(select_data[0])) #치킨 당첨자 : 11
    print("커피 당첨자 : {}".format(select_data[1:])) #커피 당첨자 : [15, 17, 8]
    print('-- 축하합니다! --')

main()

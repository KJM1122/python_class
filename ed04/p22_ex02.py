'''
택시 승객 수 구하기
'''

from random import *
def main():
    totalCnt = 0

    for passenger in range(1, 51): #1<=x<51
        time_taken = randint(5, 50) #5<=x<50
        if 5 <= time_taken <= 15: # 5<=time_taken && time_taken<=15
            print('[{0}] {1}번째 손님 (소요시간 : {2}분)'.format('O', passenger, time_taken))
            totalCnt += 1
        else:
            print(('[{0}] {1}번째 손님 (소요시간 : {2}분)'.format(' ', passenger, time_taken)))

    print('총 탑승객 : {}명'.format(totalCnt))

main()

'''
함수 호출
'''

# 마트에서 상품을 구매하는 경우
def buy(item1, item2 = '음료수'):
    print(item1, item2)

# def buy2(item1 = '음료수', item2): #오류
# non-default parameter follows default parameter
#   print(item1, item2)

def main():
    buy('과자') #과자 음료수

main()

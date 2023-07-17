'''

'''

def main():

    count = int(input("구매 상품 수를 입력하세요"))
    totalPrice = 0 #총금액

    for num in range(1, count+1):
        price = 1000
        print("2+1 상품입니다.")

        if(num % 3 == 0):
            pass
        else:
            totalPrice += price

    print('총 가격은 {}원입니다.'.format(totalPrice))

    # 구매 상품 수를 입력하세요3
    # 2+1 상품입니다.
    # 2+1 상품입니다.
    # 2+1 상품입니다.
    # 총 가격은 2000원입니다.

    # 구매 상품 수를 입력하세요6
    # 2+1 상품입니다.
    # 2+1 상품입니다.
    # 2+1 상품입니다.
    # 2+1 상품입니다.
    # 2+1 상품입니다.
    # 2+1 상품입니다.
    # 총 가격은 4000원입니다.

main()

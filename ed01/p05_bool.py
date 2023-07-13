'''
불 자료형 : 참(True) / 거짓(False)
'''

def main():
    x = True
    y = False

    # .format에 순서 인덱스 생략하면 순서대로 출력됨
    print("{} {}".format(x, type(x))) #True <class 'bool'>
    print("{} {}".format(y, type(y))) #False <class 'bool'>

    print(5 > 10) #False
    print(5 < 10) #True

    # nor 연산자 : True -> False, False -> True
    print(not True) #False
    print(not False) #True


main()

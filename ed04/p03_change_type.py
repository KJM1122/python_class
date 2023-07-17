'''
자료구조 변환
'''

def main():
    menu = {'아이스아메리카노', '모히토', '수박주스'} #중괄호는 set
    print(menu, type(menu)) #{'수박주스', '모히토', '아이스아메리카노'} <class 'set'>

    # set -> list (리스트로 변환)
    menu = list(menu) #대괄호는 list
    print(menu, type(menu)) #['수박주스', '모히토', '아이스아메리카노'] <class 'list'>

    # list -> tuple (튜플로 변환)
    menu = tuple(menu) #소괄호는 tuple
    print(menu, type(menu)) #('아이스아메리카노', '모히토', '수박주스') <class 'tuple'>

    # tuple -> set (set으로 변환)
    menu = set(menu)
    print(menu, type(menu)) #{'수박주스', '아이스아메리카노', '모히토'} <class 'set'>


main()

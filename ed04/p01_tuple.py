'''
튜플
'''

def main():
    menu = ("돈까스", "냉모밀", "라멘", "순대국")
    print(menu[0]) #돈까스
    print(menu[1]) #냉모밀
    print(menu[2]) #라멘
    print(menu[3]) #순대국

    # menu = ("1")
    # print(menu[0])
    # print(menu[1]) #오류

    name = "정민"
    age = 22
    hobby = '코딩'

    print(name,age,hobby) #정민 22 코딩 (한 칸씩 space됨)

    (name,age,hobby) = ("정민",22,'코딩')
    print(name,age,hobby) #정민 22 코딩 (한 칸씩 space됨)

    (start,end) = ("용산","춘천")
    print(start,">",end) #용산 > 춘천

    (start, end) = (end,start)
    print(start,">",end) #춘천 > 용산


main()

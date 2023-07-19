'''
문제
'''


def main():
    # split()
    str01 = "스프링|파이썬"
    print(str01.split("|"))  # list로 출력 ['스프링', '파이썬']

    str02 = "스프링 파이썬"
    print(str02.split())  # ['스프링', '파이썬']

    # endswith()
    str03 = "이 문장은 마침표로 끝나요."
    if str03.endswith("."):
        print("마침표")

    print('-' * 50)

    with open("class.txt", "w", encoding="utf8") as class_file:  # encoding="utf-8"
        class_file.write("초록반 5세 20명 파랑반 6세 18명 노랑반 7세 22명")

    with open("class.txt", "r", encoding="utf8") as class_file:
        class_list = class_file.read().split()
        print(class_list)

        for i in class_list:
            print(i, end=" ")
            if i.endswith("명"):
                print()

        print('-' * 50)

        for i in class_list:
            if i.endswith("명"):
                print(i)
            else:
                print(i, end=" ")

        # 초록반 5세 20명
        # 파랑반 6세 18명
        # 노랑반 7세 22명


main()

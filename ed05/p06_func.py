'''
매개 변수를 지정하여 호출
'''


def add(a, b):
    return a + b


def main():
    result = add(a=12, b=14)
    print(result)  # 26

    result = add(b=14, a=12)
    print(result)  # 26


main()

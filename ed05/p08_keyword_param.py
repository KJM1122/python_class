'''
키워드 파라미터
'''


def print_kwargs(**kwargs):
    print(kwargs, type(kwargs)) # 딕셔너리 타입


def main():
    print_kwargs(a=1)  # {'a': 1} <class 'dict'>
    print_kwargs(name='정민', age=22) # {'name': '정민', 'age': 22} <class 'dict'>


main()

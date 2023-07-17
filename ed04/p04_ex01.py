'''
자료구조 문제
중복 과목을 없애는 프로그램
'''

def main():
    class_subject = ['자료구조', '알고리즘', '운영체제', '알고리즘', '운영체제', '알고리즘']
    print(class_subject, type(class_subject)) #['자료구조', '알고리즘', '운영체제', '알고리즘', '운영체제', '알고리즘'] <class 'list'>

    class_subject = set(class_subject)
    print(class_subject, type(class_subject)) #{'자료구조', '운영체제', '알고리즘'} <class 'set'>

    print('-' * 50)

    # list
    application_subject = ['자료구조', '알고리즘', '자료구조', '운영체제']
    print(application_subject, type(application_subject)) #['자료구조', '알고리즘', '자료구조', '운영체제'] <class 'list'>

    # set 중복 제거
    application_subject = set(application_subject)
    print(application_subject, type(application_subject)) #{'자료구조', '운영체제', '알고리즘'} <class 'set'>

    # list로 관리
    application_subject = list(application_subject)
    print(application_subject, type(application_subject)) #['자료구조', '운영체제', '알고리즘'] <class 'list'>


main()

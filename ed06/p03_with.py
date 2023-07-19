'''
with
'''


def main():
    # 새로운 파일 생성
    with open('study.txt', 'w', encoding='utf8') as study_file:
        study_file.write("파이썬을 열심히 공부하고 있어요.")
        study_file.write("흐엥\n")
        study_file.write("정처기 제발.\n")

    # 새로운 study.txt 파일 읽기
    with open('study.txt', 'r', encoding='utf8') as study_file:
        print(study_file.read())

    # 파이썬을 열심히 공부하고 있어요.흐엥
    # 정처기 제발.


main()

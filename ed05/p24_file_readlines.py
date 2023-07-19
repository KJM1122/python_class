'''
readlines
'''


def main():
    score_file = open("score.txt", "r", encoding="utf8")

    lines = score_file.readlines()  # 파일에 있는 모든 줄을 읽어와 list로 리턴

    for line in lines:  # lines에 내용이 있을 때까지 반복
        print(line, end="")  # 읽어 온 내용 출력

    score_file.close()  # 파일 객체 닫기

    # 점심 : 닭곰탕
    # 음료 : 아메리카노
    # 과학: 80
    # 코딩: 100


main()

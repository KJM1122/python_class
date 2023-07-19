'''
readline
'''


def main():
    score_file = open("score.txt", "r", encoding="utf8")
    print(score_file.readline(), end="")  # end 값을 ""설정해 줄 바꿈 중복 수행 방지
    print(score_file.readline(), end="")  # readline: 한 줄 읽어오고 라인 스킵
    print(score_file.readline(), end="")
    print(score_file.readline(), end="")

    score_file.close()

    # 점심 : 닭곰탕
    # 음료 : 아메리카노
    # 과학: 80
    # 코딩: 100


main()

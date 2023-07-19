'''
append
'''


def main():
    score_file = open("score.txt", "a", encoding="utf8")  # 기존 파일에 내용 추가

    score_file.write("과학: 80\n")
    score_file.write("코딩: 100\n")

    score_file.close()


main()

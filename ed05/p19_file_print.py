'''
write
'''


def main():
    score_file = open("score.txt", "w", encoding="utf8")
    print("점심 : 닭곰탕", file=score_file)  # score.txt 파일에 내용 쓰기
    print("음료 : 아메리카노", file=score_file)

    score_file.close()  # score.txt 닫기


main()

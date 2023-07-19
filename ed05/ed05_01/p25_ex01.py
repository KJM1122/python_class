'''
보고서 파일 작성
'''


def main():
    # for i in range(1, 51):
    #     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
    #         report_file.write("- " + str(i) + "주차 주간보고 -\n")
    #         report_file.write("부서 :\n")
    #         report_file.write("이름 :\n")
    #         report_file.write("업무 요약 :\n")
    #
    #     report_file.close()

    for num in range(1, 51):
        # file_name = "%d주차.txt" % num  # 서식지정자
        file_name = f"{num}주차.txt"  # format함수
        # print(file_name)
        new_file = open(file_name, "w", encoding="utf8")
        print("- {0}주차 주간보고 -".format(num), file=new_file)
        print("부서 :", file=new_file)
        print("이름 :", file=new_file)
        print("업무 요약 :", file=new_file)

        new_file.close()


main()

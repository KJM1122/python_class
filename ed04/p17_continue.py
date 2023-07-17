'''
continue
'''

def main():
    # 결석한 학생 출석번호
    absent = [2, 5]

    for student in range(1, 11):
        if student in absent:
            continue #다음 학생으로 넘어 감
        print("{0}번 학생, 책을 읽어 보세요.".format(student))

    # 1번 학생, 책을 읽어 보세요.
    # 3번 학생, 책을 읽어 보세요.
    # 4번 학생, 책을 읽어 보세요.
    # 6번 학생, 책을 읽어 보세요.
    # 7번 학생, 책을 읽어 보세요.
    # 8번 학생, 책을 읽어 보세요.
    # 9번 학생, 책을 읽어 보세요.
    # 10번 학생, 책을 읽어 보세요.

main()

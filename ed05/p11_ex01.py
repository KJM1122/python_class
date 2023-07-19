'''
문제
'''


def std_weight(height, gender):
    if gender == '남자':
        weight = height * height * 22
        print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height * 100, gender, round(weight, 2)))
    elif gender == '여자':
        weight = height * height * 21
        print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height * 100, gender, round(weight, 2)))
    else:
        print("다시 입력해 주세요.")


def std_weight2(height, gender):
    if gender == '남자':
        return round(height / 100 * height / 100 * 22, 2)
    elif gender == '여자':
        return round(height / 100 * height / 100 * 21, 2)


def main():
    std_weight(1.75, '남자')  # 키 175.0cm 남자의 표준 체중은 67.38kg입니다.
    std_weight(1.6, '여자')  # 키 160.0cm 여자의 표준 체중은 53.76kg입니다.

    height = 175
    weight = std_weight2(height, '남자')
    print("키 {0}cm 남자의 표준 체중은 {1}kg입니다.".format(height, weight))
    # 키 175cm 남자의 표준 체중은 67.38kg입니다.


main()

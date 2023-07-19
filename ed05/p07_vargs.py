'''
가변 인자
'''


def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름: {0}\t나이:{1}".format(name, age), end="\t")  # end="\n"
    print("언어: " + lang1, lang2, lang3, lang4, lang5, sep=" ")  # sep=" "


def profile2(name, age, *language):
    print("이름: {0}\t나이:{1}".format(name, age), end="\t")
    print(language, type(language))


def main():
    profile('찰리', 20, '파이썬', '자바', 'C', 'C++', 'C#')
    profile('루시', 25, '코틀린', '스위프트', '', '', '')
    print('-' * 50)
    profile2('찰리', 20, '파이썬', '자바', 'C', 'C++', 'C#', 'Javascript') # 계속 추가 가능
    profile2('루시', 25, '코틀린', '스위프트')


# 이름: 찰리	나이:20	언어: 파이썬 자바 C C++ C#
# 이름: 루시	나이:25	언어: 코틀린 스위프트
# --------------------------------------------------
# 이름: 찰리	나이:20	('파이썬', '자바', 'C', 'C++', 'C#', 'Javascript') <class 'tuple'>
# 이름: 루시	나이:25	('코틀린', '스위프트') <class 'tuple'>

main()

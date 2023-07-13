'''
세로 편집 : Alt + Shift + a
'''

def main():
    name = "연탄이"
    animal = '개'
    age = 4
    is_male = True

    # 숫자와 문자열 결합은 숫자를 문자열로 캐스팅 필요
    # TypeError: can only concatenate str (not "int") to str
    # bool과 문자열 결합은 bool을 문자열로 캐스팅 필요
    # TypeError: can only concatenate str (not "bool") to str

    print("반려동물을 소개해 주세요.")
    print("우리 집 반려동물은 " + animal + "인데, 이름이 " + name + "예요.")
    print(name + "는 " + str(age) + "살이고, 산책을 아주 좋아해요.")
    print(name + "는 " + str(is_male) + " 수컷인가요?")
    print("네.")


main()

    # 반려동물을 소개해 주세요.
    # 우리 집 반려동물은 개인데, 이름이 연탄이예요.
    # 연탄이는 4살이고, 산책을 아주 좋아해요.
    # 연탄이는 True 수컷인가요?
    # 네.
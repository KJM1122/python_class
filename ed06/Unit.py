class Unit:
    def __init__(self, name, hp, damage):
        # 인스턴스 변수: self.변수명 = 값
        self.name = name  # 인스턴스 변수 name에 전달값 name을 할당
        self.hp = hp
        self.damage = damage

        print("{0} 유닛을 생성했습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


# 객체 생성: 객체명 = 클래스명(전달값1, 전달값2, ...)
soldier1 = Unit('보병', 40, 5)
soldier2 = Unit('보병', 40, 5)
tank1 = Unit('탱크', 150, 35)
stealth1 = Unit('전투기', 80, 5)
# 보병 유닛을 생성했습니다.
# 체력 40, 공격력 5
# 보병 유닛을 생성했습니다.
# 체력 40, 공격력 5
# 탱크 유닛을 생성했습니다.
# 체력 150, 공격력 35
# 전투기 유닛을 생성했습니다.
# 체력 80, 공격력 5

# 인스턴스 변수에 접근
print('유닛 이름: {0}, 공격력: {1}'.format(stealth1.name, stealth1.damage))
# 유닛 이름: 전투기, 공격력: 5

# 특별한 인스턴스 변수 정의: 은폐 기능 추가
stealth2 = Unit('전투기', 80, 5)
stealth2.cloaking = True
if stealth2.cloaking == True:
    print("{0}는 현재 은폐 상태입니다.".format(stealth2.cloaking))
# if stealth1.cloaking == True:
#     print("{0}는 현재 은폐 상태입니다.".format(stealth1.cloaking))
#     # AttributeError: 'Unit' object has no attribute 'cloaking'

# 전투기 유닛을 생성했습니다.
# 체력 80, 공격력 5
# True는 현재 은폐 상태입니다.
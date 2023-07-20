class Unit:
    def __init__(self, name, hp):
        # 인스턴스 변수: self.변수명 = 값
        self.name = name  # 인스턴스 변수 name에 전달값 name을 할당
        self.hp = hp  # 인스턴스 변수 hp 전달값 hp 할당


class AttackUnit(Unit):  # Unit 상속받음
    # 생성자 첫 번째 인자는 self
    def __init__(self, name, hp, damage):
        # 부모 클래스의 생성자 호출
        Unit.__init__(self, name, hp)
        self.damage = damage

    # 메서드 첫 번째 인자는 self
    def attack(self, location):
        # \ 공간이 좁아 2줄로 표시
        print('{0}: {1}시 방향 적군을 공격합니다. [공격력: {2}]' \
              .format(self.name, location, self.damage))

    def damaged(self, damage):
        print('{0}: {1}만큼 피해를 입었습니다.'.format(self.name, damage))
        # 유닛의 체력에서 전달받은 damage만큼 감소
        self.hp -= damage
        print('{0}: 현재 체력은 {1}입니다.'.format(self.name, self.hp))

        if self.hp <= 0:
            print('{0}: 파괴됐습니다.'.format(self.name))


# 테스트
flamethrower1 = AttackUnit('화염방사병', 50, 16)
flamethrower1.attack(5)
flamethrower1.damaged(25)
flamethrower1.damaged(25)

# 화염방사병: 5시 방향 적군을 공격합니다. [공격력: 16]
# 화염방사병: 25만큼 피해를 입었습니다.
# 화염방사병: 현재 체력은 25입니다.
# 화염방사병: 25만큼 피해를 입었습니다.
# 화염방사병: 현재 체력은 0입니다.
# 화염방사병: 파괴됐습니다.
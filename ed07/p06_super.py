class Unit:
    def __init__(self, name, hp, speed):
        # 인스턴스 변수(self.변수명) = 값(파라미터)
        self.name = name  # 인스턴스 변수 name에 전달값 name을 할당
        self.hp = hp  # 인스턴스 변수 hp 전달값 hp 할당
        self.speed = speed  # 인스턴스 변수 speed 전달값 speed 할당

    def move(self, location):
        print('[지상 유닛 이동]')
        print('{0}: {1}시 방향으로 이동합니다. [속도: {2}]'.format(self.name, location, self.speed))


class AttackUnit(Unit):  # Unit 상속받음
    # 생성자 첫 번째 인자는 self
    def __init__(self, name, hp, damage, speed):  # 생성자에 speed 추가
        # 부모 클래스의 생성자 호출
        Unit.__init__(self, name, hp, speed)
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


class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print('{0}: {1}시 방향으로 날아갑니다. [속도: {2}]'.format(name, location, self.flying_speed))


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0)  # 지상 이동 속도 0
        Flyable.__init__(self, flying_speed)

    # Unit에 있는 move()메서드 오버라이딩
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)  # 지상 건물 속도: 0 (건물은 지상 이동 불가)
        super().__init__(name, hp, 0)  # super일 때는 self 생략 가능
        self.location = location


supply_depot = BuildingUnit("보급고", hp=500, location=7)

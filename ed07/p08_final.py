class Unit:
    def __init__(self, name, hp, speed):
        # 인스턴스 변수(self.변수명) = 값(파라미터)
        self.name = name  # 인스턴스 변수 name에 전달값 name을 할당
        self.hp = hp  # 인스턴스 변수 hp 전달값 hp 할당
        self.speed = speed  # 인스턴스 변수 speed 전달값 speed 할당

        # $1 안내 문구 출력
        print('{0} 유닛을 생성했습니다.'.format(name))

    def move(self, location):
        # $2 출력문 삭제
        # print('[지상 유닛 이동]')
        print('{0}: {1}시 방향으로 이동합니다. [속도: {2}]'.format(self.name, location, self.speed))

    # $3 AttackUnit에 있던 damaged() 메서드 이동
    def damaged(self, damage):
        print('{0}: {1}만큼 피해를 입었습니다.'.format(self.name, damage))
        # 유닛의 체력에서 전달받은 damage만큼 감소
        self.hp -= damage
        print('{0}: 현재 체력은 {1}입니다.'.format(self.name, self.hp))

        if self.hp <= 0:
            print('{0}: 파괴됐습니다.'.format(self.name))


# 공격 유닛
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

    ''' #$4 여러 줄 comment
        def damaged(self, damage):
        print('{0}: {1}만큼 피해를 입었습니다.'.format(self.name, damage))
        # 유닛의 체력에서 전달받은 damage만큼 감소
        self.hp -= damage
        print('{0}: 현재 체력은 {1}입니다.'.format(self.name, self.hp))

        if self.hp <= 0:
            print('{0}: 파괴됐습니다.'.format(self.name))
    '''


# 탱크 유닛
class Tank(AttackUnit):
    # 클래스 변수: 클래스명 바로 밑에 정의, 클래스로부터 만들어진 모든 객체에 값이 일괄 적용됨
    siege_developed = False  # 시지모드 개발 여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", hp=150, damage=35, speed=1)
        self.siege_mode = False  # 시지모드 해지상태, 인스턴스 변수로 정의

    def set_siege_mode(self):
        # 시지모드가 개발되어있지 않으면 바로 return
        if Tank.siege_developed == False:  # 클래스 변수 접근방법: 클래스명.클래스변수
            return

        # 현재 일반모드일 때 시지모드로 전환
        if self.siege_mode == False:
            print('{0}: 시지모드로 전환합니다.'.format(self.name))

            # 공격력 2배 증가
            self.damage *= 2

            # 시지모드 설정
            self.siege_mode = True

        # 시지모드일 때 일반모드로 전환
        else:
            print('{0}: 시지모드를 해제합니다.'.format(self.name))

            # 공격력 절반으로 감소
            self.damage //= 2  # 몫만 취함

            # 시지모드 해제
            self.siege_mode = False


# 보병 유닛
class Soldier(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "보병", hp=40, damage=5, speed=1)

    def booster(self):
        if self.hp >= 10:
            self.hp -= 10  # 체력을 10만큼 감소
            print('{0}: 강화제를 사용합니다. (HP 10 감소)'.format(self.name))
        else:
            print('{0}: 체력이 부족해 강화제를 사용할 수 없습니다.'.format(self.name))


# 공중 유닛
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


# 전투기 유닛
class Stealth(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, '전투기', hp=80, damage=20, flying_speed=5)
        self.cloacked = False  # 은폐모드(해제 상태), 인스턴스 변수

    def claking(self):
        # 은폐모드일 때 은폐모드 해제
        if self.cloacked == True:
            print('{0}: 은폐모드를 해제합니다.'.format(self.name))
            self.cloacked = False
        else:
            print('{0}: 은폐모드를 설정합니다.'.format(self.name))
            self.cloacked = True


# 건물 유닛
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)  # 지상 건물 속도: 0 (건물은 지상 이동 불가)
        super().__init__(name, hp, 0)  # super일 때는 self 생략 가능
        self.location = location


# 게임 시작
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")


# 게임 종료
def game_over():
    print("Player : Good Game")
    print("[Player]님이 게임에서 퇴장했습니다.")


'''
1. 게임 시작
2. 유닛 생성 (보병 3, 탱크 2, 전투기 1)
3. 전군 1시 방향으로 이동
4. 탱크 시지모드 개발
5. 공격 준비 (보병 강화제, 탱크 시지모드, 전투기 은폐모드)
6. 전군 1시 방향 공격
7. 전군 피해
8. 게임 종료
'''
def main():
    pass


main()

'''
스타크래프트
'''


# 공격 함수
def attack(name, location, damage):
    print("{0}: {1}시 방향 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))


def main():
    # 보병: 공격 유닛, 군인, 총을 쏠 수 있음
    name = '보병'
    hp = 40
    damage = 5

    print("{} 유닛을 생성했습니다.".format(name))
    print("체력 {0}, 공격력 {1}\n".format(hp, damage))

    # 탱크: 공격 유닛, 포를 쏠 수 있음, 두 가지 모드(일반/시지 모드)
    tank_name = '탱크'
    tank_hp = 150
    tank_damage = 35

    print("{} 유닛을 생성했습니다.".format(tank_name))
    print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

    # 새로운 탱크2 추가
    tank2_name = '탱크'
    tank2_hp = 150
    tank2_damage = 35

    print("{} 유닛을 생성했습니다.".format(tank2_name))
    print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

    print('-' * 50)

    # 보병과 탱크가 1시 방향으로 공격하도록 명령
    attack(name, 1, damage)
    attack(tank_name, 1, tank_damage)
    attack(tank2_name, 1, tank_damage)

    # 보병 유닛을 생성했습니다.
    # 체력 40, 공격력 5
    #
    # 탱크 유닛을 생성했습니다.
    # 체력 150, 공격력 35
    #
    # 탱크 유닛을 생성했습니다.
    # 체력 150, 공격력 35
    #
    # --------------------------------------------------
    # 보병: 1시 방향 적군을 공격합니다. [공격력 5]
    # 탱크: 1시 방향 적군을 공격합니다. [공격력 35]
    # 탱크: 1시 방향 적군을 공격합니다. [공격력 35]


main()

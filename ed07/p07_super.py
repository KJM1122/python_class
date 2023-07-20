class Unit:
    def __init__(self):
        print('Unit 생성자')


class Flyable:
    def __init__(self):
        print('Flyable 생성자')


class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__()  # 순서상 가장 먼저 상속받은 클래스에 접근됨
        # 다중 상속시 각 부모클래스의 이름을 명시해서 접근하는 것이 원칙
        Unit.__init__(self)  # Unit 생성자
        Flyable.__init__(self)  # Flyable 생성자


troopship = FlyableUnit()

'''
pass
'''


# 함수에 pass 키워드 사용
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")


def game_stop():
    pass  # 함수에 pass 키워드 사용


def main():
    game_start()  # [알림] 새로운 게임을 시작합니다.
    game_stop()


main()

'''
외장 함수
'''
import glob


def main():
    print(glob.glob("*.py"))  # 현재 디렉토리에 있는 파이썬 파일 찾기
    # ['p01_internal_func.py', 'p02_external_func.py']


main()

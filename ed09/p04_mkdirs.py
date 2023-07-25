'''
디렉토리 생성
'''
import os.path


def main():
    folder = '2023'

    if os.path.exists(folder):  # 같은 이름의 폴더가 존재하면
        print('이미 폴더가 존재합니다.')
    else:  # 폴더가 없으면
        os.makedirs(folder)
        print(folder, '폴더를 생성했습니다.')
        # ed09 안에 2023 폴더 생성


main()

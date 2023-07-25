'''
getfile()
'''

import inspect
from travel import *


def main():
    print(inspect.getfile(thailand))  # thailand 모듈 위치(경로)
    # __name__: travel_temp.thailand
    # 이 문장은 외부에서 모듈 실행 시 출력
    # C:\JSPA_0309\04_PYTHON\04_01_PYTHON\workspace\travel_temp\thailand.py

    # __name__: travel.thailand
    # 이 문장은 외부에서 모듈 실행 시 출력
    # C:\Python38\lib\travel\thailand.py


main()

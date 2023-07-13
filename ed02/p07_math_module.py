'''
math 모듈
'''
from math import * #(math 모듈의 모든 기능 사용)
# from math import floor, ceil, sqrt #(math 모듈에서 floor, ceil, sqrt 사용)

def main():
    result = floor(4.99) #내림
    print(result) #4

    # math.ceil(3.14)
    result = ceil(3.14) #올림
    print(result) #4

    result = sqrt(16) #제곱근
    print(result) #4.0


main()

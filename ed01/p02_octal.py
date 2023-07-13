'''
숫자형: 진수
'''

def main():
    # 8진수(Octal) 숫자0 + 소문자o = 0o
    num = 0o177
    print("{0}의 자료형은 {1}".format(num, type(num))) #127의 자료형은 <class 'int'>

    # 16진수(Hex) 숫자0 + 소문자x/대문자X = 0x/0X
    num = 0XB
    print("{0}의 자료형은 {1}".format(num, type(num))) #11의 자료형은 <class 'int'>


main()
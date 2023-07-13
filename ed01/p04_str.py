'''
문자열
'''

def main():
    print('풍선') #풍선
    print("나비") #나비
    print("나비" * 5) #나비나비나비나비나비
    print("10") #10
    #print('문법 오류")
    #print("문법 오류')

    # 문자열 내에 작은 따옴표
    print("I don't want to go to school.") #I don't want to go to school.
    #print('I don't want to go to school.') #문법 오류

    # 이스케이프 코드 : \'
    print('I don\'t want to go to school.') #I don't want to go to school.

    # 여러 줄인 문자열을 변수에 대입하고 싶을 때
    # 이스케이프 코드 : \n
    # ctrl + / : comment

    multiline = "Life is too short\nYou need Python"
    print(multiline)
    # Life is too short
    # You need Python

    # ''' '''
    multiline = '''
    Life is too short
    You need Python
    '''
    print(multiline)
    #
    # Life is too short
    # You need Python
    #


main()

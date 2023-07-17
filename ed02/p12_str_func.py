'''
문자열 처리 함수
'''

def main():
    python = 'Python is Amazing.'

    print(python.lower()) #python is amazing.
    print(python.upper()) #PYTHON IS AMAZING.
    print(python[1:3].islower()) #인덱스 1번부터 2번까지 소문자인지 확인 #True

    # Python을 Java로 변환
    print(python.replace('Python', "Java")) #Java is Amazing.

    print(python) #Python is Amazing.

    # find(찾는 문자, 시작인덱스, 종료인덱스): 찾는 문자가 없으면 -1
    find = python.find('n')
    print(find) #5 (첫 번째 찾은 위치의 인덱스인 5 리턴)

    find = python.find('n', find + 1) #문자 인덱스 6번째부터 찾아 n이 발견된 위치
    print(find) #15

    # 존재하지 않는 문자 찾기
    find = python.find('java')
    print(find) #-1

    print('-' * 50)

    # index(찾는 문자, 시작인덱스, 종료인덱스): 찾는 문자 없으면 예외 발생
    index = python.index("n")
    print(index) #5

    index = python.index("n", index + 1)
    print(index) #15

    index = python.index("n", 2, 6)
    print(index) #5

    # 존재하지 않는 문자 찾기
    #index = python.index("Spring")
    #print(index)
    ##ValueError: substring not found

    # count() : 문자열의 총 개수
    print(python) #Python is Amazing.
    print(python.count("n")) #2
    print(python.count("v")) #0

    # len(변수 또는 문자열) : 문자열의 길이
    print(len(python)) #18

    # strip() : 앞뒤 공백 제거
    a = " hi "
    print(a.strip()) #hi

    # split() : 문자열 나누기
    b = "Life is too short."
    print(b.split()) #['Life', 'is', 'too', 'short.']


main()
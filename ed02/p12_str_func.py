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


main()

'''
함수 호출
'''

def profile(name, age = 20, main_lang = 'Java'): #default값 세팅 가능
    print("이름: {0}\t\t나이: {1}\t\t언어: {2}".format(name, age, main_lang))

def main():
    profile("정민", 22, "Java")
    profile("정민", 23, "Python")
    profile("정민", 22)
    profile("정민")

# 이름: 정민		나이: 22		언어: Java
# 이름: 정민		나이: 23		언어: Python
# 이름: 정민		나이: 22		언어: Java
# 이름: 정민		나이: 20		언어: Java

main()

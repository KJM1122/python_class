'''
첫 번째 글자는 대문자, 나머지 글자는 소문자
'''

def main():
    str1 = "the early bird catches the worm."
    str2 = "Actions Speak Louder Than Words."
    str3 = "PRACTICE MAKES PERFECT."

    print(str1[0].upper() + str1[1:].lower()) #The early bird catches the worm.
    print(str2[0].upper() + str2[1:].lower()) #Actions speak louder than words.
    print(str3[0].upper() + str3[1:].lower()) #Practice makes perfect.

    print('-' * 50)

    sentence01 = "The early bird catches the worm."
    sentence02 = "Actions speak louder than words."
    sentence03 = "Practice makes perfect."

    print(sentence01.lower()) #the early bird catches the worm.

    print(sentence02.title()) #Actions Speak Louder Than Words.
    arrayStr = sentence02.split()
    for i in arrayStr:
        print(i.capitalize(), end=' ') #Actions Speak Louder Than Words.
    print('')

    print(sentence03.upper()) #PRACTICE MAKES PERFECT.

main()

'''
사이트 별로 비밀번호를 생성하는 프로그램
'''

def main():
    naver = "http://naver.com"
    daum = "http://daum.net"
    google = "http://google.com"
    youtube = "http://youtube.com"

    httpLen = len("http://") #7 (http://의 길이)
    dotIndex = naver.find('.')

    print(naver + "의 비밀번호는 " + naver[httpLen:httpLen+3] + str(len(naver[httpLen:dotIndex])) + str(naver.count('e')) + "!입니다.")
    print(daum + "의 비밀번호는 " + daum[httpLen:httpLen+3] + str(len(daum[httpLen:dotIndex])) + str(daum.count('e')) + "!입니다.")
    print(google + "의 비밀번호는 " + google[httpLen:httpLen+3] + str(len(google[httpLen:dotIndex])) + str(google.count('e')) + "!입니다.")
    print(youtube + "의 비밀번호는 " + youtube[httpLen:httpLen+3] + str(len(youtube[httpLen:dotIndex])) + str(youtube.count('e')) + "!입니다.")

    # http://naver.com의 비밀번호는 nav51!입니다.
    # http://daum.net의 비밀번호는 dau51!입니다.
    # http://google.com의 비밀번호는 goo51!입니다.
    # http://youtube.com의 비밀번호는 you51!입니다.

    print('-' * 50)

    url = "http://naver.com"
    startIdx = url.find("/")
    print(startIdx + 2) #7
    startIdx += 2

    endIdx = url.find(".")

    findWord = url[startIdx:endIdx]
    print(findWord) #naver

    nameThree = findWord[:3] #처음 3글자
    namelen = len(findWord) #글자 개수
    eCount = findWord.count('e') #글자 내 'e'의 개수
    spChar = "!" #스페셜 char

    print("{0}의 비밀번호는 {1}{2}{3}{4}입니다.".format(url, nameThree, namelen, eCount, spChar))

main()

'''
셀레니움 테스트
'''
from selenium import webdriver


def main():
    # web driver 객체 생성 : 같은 경로에 chromedriver.exe가 있을 때
    driver = webdriver.Chrome()

    url = 'https://www.naver.com'

    driver.get(url)


main()

'''
셀레니움 네이버 로그인
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyperclip3  # 클립보드 사용 외부 모듈
import time


def naver_login():
    url = "https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/"

    # 웹 드라이버 실행
    browser = webdriver.Chrome()

    # 접속
    browser.get(url)
    user_id = 'kimjmin1122'
    user_pw = ''

    # id
    id_text_input = browser.find_element(By.ID, 'id')
    id_text_input.click()
    pyperclip3.copy(user_id)  # 클립보드로 user_id 값 가져옴
    id_text_input.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)  # 1초간 sleep

    # 비밀번호
    pw_text_input = browser.find_element(By.ID, 'pw')
    pw_text_input.click()
    pyperclip3.copy(user_pw)  # 클립보드로 user_pw 값 가져옴
    pw_text_input.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)  # 1초간 sleep

    # 로그인 버튼
    btn_login = browser.find_element(By.ID, 'log.login')
    btn_login.click()
    time.sleep(5)

    # while True:
    #     pass

    # 드라이버 종료
    # browser.quit()


def main():
    naver_login()


main()

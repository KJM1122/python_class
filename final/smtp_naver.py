'''
파일명 : smtp.naver.py
설명 : naver smtp를 이용해서 메일 전송, csv에서 파일 읽어 전송
생성일 : 2023-07-25
생성자 : KJM
(c) 2023. KJM all rights reserved.
'''
import smtplib
from email.mime.text import MIMEText


def read_addressbook():
    mail_list = []  # CSV 파일을 한 줄씩 담기

    try:
        with open('address.csv', 'r') as f:
            i = 0
            while True:
                line = f.readline()
                print(line, end='')
                if not line:  # line이 True가 아니면 break
                    break
                mail_list.append(line.strip("\n"))  # \n 제거
    except IOError as e:
        pass
    finally:
        print('CSV 파일 읽기 완료!')

    return mail_list


def naver_smtp(name, receive_email, p_title, p_contents):
    s = None  # smtplib.SMTP_SLL 객체
    try:
        smtp_name = 'smtp.naver.com'  # SMTP 서버명
        smtp_port = 465  # SMTP 포트
        send_email = 'kimjmin1122@naver.com'  # 보내는 사람 이메일
        password = ''
        recv_email = receive_email  # 받는 사람 이메일
        title = p_title
        contents = p_contents
        # 이름을 붙여서 전송
        contents = '{0}님\n{1}'.format(name, contents)

        msg = MIMEText(contents)
        msg['From'] = send_email  # 보내는 사람
        msg['To'] = recv_email  # 받는 사람
        msg['Subject'] = title  # 제목

        s = smtplib.SMTP_SSL(smtp_name, smtp_port)  # SMTP 서버명, SMTP 포트
        s.set_debuglevel(True)  # 디버그 메시지 출력

        s.login(send_email, password)  # 로그인
        s.sendmail(send_email, recv_email, msg.as_string())

    except Exception as e:
        print(f'예외 {e}')
    finally:
        if s is not None:
            s.close()


if __name__ == '__main__':
    name = '정민'
    receive_email = 'kimjmini1122@gmail.com'
    p_title = '테스트 메일'
    p_contents = '내용'
    # naver_smtp(name, receive_email, p_title, p_contents)

    mail_list = read_addressbook()

    print('---main---')
    for m_data in mail_list[1:]:  # CSV 파일 첫 줄 건너뛰기
        # print(m_data)
        list_str = m_data.split(",")
        # print(list_str)
        naver_smtp(name=list_str[1], receive_email=list_str[2], p_title=list_str[3], p_contents=list_str[4])

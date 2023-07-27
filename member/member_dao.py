'''
파일명: memeber_dao.py
생성자: PCWK
생성일: 2023-07-27
'''
import oracledb

from common.work_div import WorkDiv  # common 패키지 안의 work_div.py의 WorkDiv 패키지
from member_vo import MemberVO


class MemberDao(WorkDiv):

    # 생성자
    def __init__(self):
        # DB Connection 변수
        self.conn = None

    # DB 연결
    def connect_db(self):
        try:
            self.conn = oracledb.connect(user='scott', password='pcwk', dsn='192.168.0.18:1521/XE')  # DB Connection
        except Exception as e:
            print('-' * 50)
            print('connect_db:{}'.format(e))
            print('-' * 50)

    # DB 자원 반납
    def disconnect_db(self):
        try:
            self.conn.close()
        except Exception as e:
            print('-' * 50)
            print('disconnect_db:{}'.format(e))
            print('-' * 50)

    # ctrl + o (Override Methods)
    def do_save(self, member: MemberVO):  # 파라미터:타입
        flag = 0
        try:
            '''
            1. DB 연결
            2. parameter 확인
            3. cursor 생성
            4. sql 정리
            5. sql 실행
            6. transaction 처리
            7. 자원 반납
            '''
            self.connect_db()
            print('1. self.conn: {0}'.format(self.conn))
        except Exception as e:
            print('do_save:{}'.format(e))
        finally:
            print('7. do_save finally')
            self.disconnect_db()
        return flag

    def do_delete(self):
        pass

    def do_select_one(self):
        pass

    def do_update(self):
        pass

    def do_retrieve(self):
        pass


if __name__ == '__main__':
    m01 = MemberVO('lion', '라이언', '4321', 'kimjmini1122@gmail.com', '', 'lion')
    dao = MemberDao()
    dao.do_save(m01)

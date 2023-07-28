'''
파일명: memeber_dao.py
생성자: PCWK
생성일: 2023-07-27
'''
import oracledb
import common.pcwk_logging as p_log
from common.work_div import WorkDiv  # common 패키지 안의 work_div.py의 WorkDiv 패키지
from member_vo import MemberVO

'''
    flag = 0
    try:
        pass
    except oracledb.DatabaseError as e:
        p_log.logger2.debug('DatabaseError:{}'.format(e))
    except Exception as e:
        p_log.logger2.debug('Exception:{}'.format(e))
    finally:
        p_log.logger2.debug('6.  finally')
        self.disconnect_db()
    return flag
'''


class MemberDao(WorkDiv):

    # 생성자
    def __init__(self):
        # DB Connection 변수
        self.conn = None

    # DB 연결
    def connect_db(self):
        try:
            self.conn = oracledb.connect(user='scott', password='pcwk', dsn='192.168.0.18:1521/XE')  # DB Connection
            p_log.logger2.debug(self.conn)
        except Exception as e:
            print('-' * 50)
            print('connect_db:{}'.format(e))
            print('-' * 50)

    # DB 자원 반납
    def disconnect_db(self):
        try:
            self.conn.close()
        except Exception as e:
            p_log.logger2.debug('-' * 50)
            p_log.logger2.debug('disconnect_db:{}'.format(e))
            p_log.logger2.debug('-' * 50)

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
            # 1. DB 연결
            self.connect_db()
            p_log.logger2.debug('1. self.conn: {0}'.format(self.conn))

            # 2. parameter 확인
            p_log.logger2.debug('2. param: {0}'.format(member))

            # 3. cursor 생성
            cur = self.conn.cursor()
            p_log.logger2.debug('3. cur: {0}'.format(cur))

            # 4. sql 정리
            sql = '''
                INSERT INTO member (
                    user_id,
                    name,
                    passwd,
                    email,
                    reg_dt,
                    reg_id
                ) VALUES (
                    :1,
                    :2,
                    :3,
                    :4,
                    SYSDATE,
                    :5
                )
            '''
            p_log.logger2.debug('4. sql: {}'.format(sql))

            # 5. sql 실행
            cur.execute(sql, (member.user_id, member.name, member.passwd, member.email, member.reg_id))  # 튜플에 파라미터

            # 6. transaction 처리
            self.conn.commit()
            flag = cur.rowcount  # 반영된 건수
            p_log.logger2.debug('5. flag: {}'.format(flag))

        except oracledb.DatabaseError as e:
            p_log.logger2.debug('DatabaseError:{}'.format(e))
        except Exception as e:
            p_log.logger2.debug('Exception:{}'.format(e))
        finally:
            p_log.logger2.debug('6. do_save finally')
            self.disconnect_db()

        return flag

    def do_delete(self, member: MemberVO):
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
            # 1. DB 연결
            self.connect_db()
            p_log.logger2.debug('1. self.conn: {0}'.format(self.conn))

            # 2. parameter 확인
            p_log.logger2.debug('2. param: {0}'.format(member))

            # 3. cursor 생성
            cur = self.conn.cursor()
            p_log.logger2.debug('3. cur: {0}'.format(cur))

            # 4. sql 정리
            sql = 'DELETE FROM member WHERE user_id = :1'
            p_log.logger2.debug('4. sql: {}'.format(sql))

            # 5. sql 실행
            cur.execute(sql, (member.user_id,))  # 튜플에 데이터가 하나일 때 뒤에 , 필수

            # 6. transaction 처리
            self.conn.commit()
            flag = cur.rowcount  # 반영된 건수
            p_log.logger2.debug('5. flag: {}'.format(flag))

        except oracledb.DatabaseError as e:
            p_log.logger2.debug('DatabaseError:{}'.format(e))
        except Exception as e:
            p_log.logger2.debug('Exception:{}'.format(e))
        finally:
            p_log.logger2.debug('6. do_delete finally')
            self.disconnect_db()

        return flag

    def do_select_one(self, member: MemberVO):
        outVO = None  # 리스트 데이터
        vo = None  # return MemberVO
        try:
            '''
            1. DB 연결
            2. parameter 확인
            3. cursor 생성
            4. sql 정리
            5. sql 실행
            6. 데이터 조회
            7. 자원 반납
            '''
            # 1. DB 연결
            self.connect_db()
            p_log.logger2.debug('1. self.conn: {0}'.format(self.conn))

            # 2. parameter 확인
            p_log.logger2.debug('2. param: {0}'.format(member))

            # 3. cursor 생성
            cur = self.conn.cursor()
            p_log.logger2.debug('3. cur: {0}'.format(cur))

            # 4. sql 정리
            sql = '''
                SELECT
                    user_id,
                    name,
                    passwd,
                    email,
                    TO_CHAR(reg_dt, 'YYYY-MM-DD HH24:MI:SS') as reg_dt,
                    reg_id
                FROM
                    member
                WHERE user_id = :1
            '''
            p_log.logger2.debug('4. sql: {}'.format(sql))

            # 5. sql 실행
            cur.execute(sql, (member.user_id,))  # 튜플에 데이터가 하나일 때 뒤에 , 필수

            # 6. 데이터 조회 (리스트 내포)
            outVO = [MemberVO(user_id=row[0],
                              name=row[1],
                              passwd=row[2],
                              email=row[3],
                              reg_dt=row[4],
                              reg_id=row[5])
                     for row in cur]
            if None != outVO and len(outVO) > 0:
                vo = outVO[0]
                p_log.logger2.debug(
                    f'5. vo: {vo.user_id}, {vo.name}, {vo.passwd}, {vo.email}, {vo.reg_dt}, {vo.reg_id}')

        except oracledb.DatabaseError as e:
            p_log.logger2.debug('DatabaseError:{}'.format(e))
        except Exception as e:
            p_log.logger2.debug('Exception:{}'.format(e))
        finally:
            p_log.logger2.debug('6. do_select_one finally')
            self.disconnect_db()

        return vo

    def do_update(self, member: MemberVO):
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
            # 1. DB 연결
            self.connect_db()
            p_log.logger2.debug('1. self.conn: {0}'.format(self.conn))

            # 2. parameter 확인
            p_log.logger2.debug('2. param: {0}'.format(member))

            # 3. cursor 생성
            cur = self.conn.cursor()
            p_log.logger2.debug('3. cur: {0}'.format(cur))

            # 4. sql 정리
            sql = '''
                UPDATE member
                SET
                    name   = :1,
                    passwd = :2,
                    email  = :3,
                    reg_dt = SYSDATE,
                    reg_id = :4
                WHERE
                    user_id = :5
            '''
            p_log.logger2.debug('4. sql: {}'.format(sql))

            # 5. sql 실행
            cur.execute(sql, (member.name, member.passwd, member.email, member.reg_id, member.user_id))

            # 6. transaction 처리
            self.conn.commit()
            flag = cur.rowcount  # 반영된 건수
            p_log.logger2.debug('5. flag: {}'.format(flag))

        except oracledb.DatabaseError as e:
            p_log.logger2.debug('DatabaseError:{}'.format(e))
        except Exception as e:
            p_log.logger2.debug('Exception:{}'.format(e))
        finally:
            p_log.logger2.debug('6. do_update finally')
            self.disconnect_db()

        return flag

    def do_retrieve(self):
        outList = []
        try:
            '''
            1. DB 연결
            2. cursor 생성
            3. sql 정리
            4. sql 실행
            5. 데이터 조회
            6. 자원 반납
            '''
            # 1. DB 연결
            self.connect_db()
            p_log.logger2.debug('1. self.conn: {0}'.format(self.conn))

            # 2. cursor 생성
            cur = self.conn.cursor()
            p_log.logger2.debug('2. cur: {0}'.format(cur))

            # 3. sql 정리
            sql = '''
                SELECT A.*, B.*
                FROM (
                SELECT
                    TT1.rnum as num,
                    TT1.user_id,
                    TT1.name,
                    TT1.passwd,
                    TT1.email,
                    -- 당일이면 HH24:MI
                    -- 그렇지 않으면 YYYY-MM-DD
                    DECODE(TO_CHAR(TT1.reg_dt, 'YYYY-MM-DD'), TO_CHAR(SYSDATE, 'YYYY-MM-DD')
                                                            , TO_CHAR(TT1.reg_dt, 'HH24:MI')
                                                            , TO_CHAR(TT1.reg_dt, 'YYYY-MM-DD')) AS reg_dt,
                    TT1.reg_id
                FROM (
                    SELECT ROWNUM AS rnum, T1.*
                    FROM (
                        SELECT *
                        FROM member
                        --WHERE
                        ORDER BY reg_dt DESC
                    )T1
                    WHERE ROWNUM <= 10
                )TT1
                WHERE rnum >= 1
                )A
                CROSS JOIN
                (
                SELECT COUNT(*) AS total_cnt
                FROM member
                --WHERE
                )B
            '''
            p_log.logger2.debug('3. sql: {}'.format(sql))

            # 4. sql 실행
            cur.execute(sql)

            # 5. 데이터 조회 (리스트 내포)
            outList = [MemberVO(num=row[0],
                                user_id=row[1],
                                name=row[2],
                                passwd=row[3],
                                email=row[4],
                                reg_dt=row[5],
                                reg_id=row[6])
                       for row in cur]

            if None != outList and len(outList) > 0:
                for vo in outList:
                    p_log.logger2.debug('4. vo: {}'.format(vo))

        except oracledb.DatabaseError as e:
            p_log.logger2.debug('DatabaseError:{}'.format(e))
        except Exception as e:
            p_log.logger2.debug('Exception:{}'.format(e))
        finally:
            p_log.logger2.debug('5. do_retrieve finally')
            self.disconnect_db()

        return outList


if __name__ == '__main__':
    m01 = MemberVO('lion', '라이언', '4321', 'kimjmini1122@gmail.com', '', 'lion')
    dao = MemberDao()
    dao.do_save(m01)

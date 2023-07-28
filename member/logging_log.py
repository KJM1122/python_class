'''
Python의 logging 기능을 제공하는 내장 모듈로,
콘솔 로그, 파일 로그 기록 가능
프로그램 실행 중에 발생할 수 있는 정보, 경고, 오류 기록
DEBUG > INFO > WARNING > ERROR > CRITICAL
'''

# logging 모듈 가져오기
import logging

# formatter = logging.Formatter('%(asctime)s [%(filename)s:%(lineno)s|%(levelname)s] %(funcName)s(): %(message)s')
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s [%(filename)s:%(lineno)s|%(levelname)s] %(funcName)s(): %(message)s')  # output level
log = logging.getLogger(__name__)

# asctime : 로그 기록 시간
# lineno : 라인 번호
# function : 함수 이름
# message : 메시지

if __name__ == '__main__':
    log.critical('critical')
    log.error('error')
    log.warning('warning')
    log.info('info')
    log.debug('debug')

# level=logging.ERROR
# CRITICAL:__main__:critical
# ERROR:__main__:error

# level=logging.DEBUG
# CRITICAL:__main__:critical
# ERROR:__main__:error
# WARNING:__main__:warning
# INFO:__main__:info
# DEBUG:__main__:debug

# 2023-07-28 10:36:36,121 [logging_log.py:22|CRITICAL] <module>(): critical
# 2023-07-28 10:36:36,121 [logging_log.py:23|ERROR] <module>(): error
# 2023-07-28 10:36:36,121 [logging_log.py:24|WARNING] <module>(): warning
# 2023-07-28 10:36:36,121 [logging_log.py:25|INFO] <module>(): info
# 2023-07-28 10:36:36,121 [logging_log.py:26|DEBUG] <module>(): debug
'''
파일명: memeber_vo.py
생성자: PCWK
생성일: 2023-07-27
'''
from common.dto import DTO


class MemberVO(DTO):
    # 생성자
    def __init__(self, user_id, name, passwd, email, reg_dt=None, reg_id=None, num=0):
        super().__init__(num)  # DTO의 num 호출
        self.user_id = user_id  # 아이디
        self.name = name  # 이름
        self.passwd = passwd  # 비밀번호
        self.email = email  # 이메일
        self.reg_dt = reg_dt  # 등록일
        self.reg_id = reg_id  # 등록자

    # 인스턴스 변수들을 문자열로 변환
    def __str__(self):
        return 'num:{}, user_id:{}, name:{}, passwd:{}, email:{}, reg_dt:{}, reg_id:{}' \
            .format(self.num, self.user_id, self.name, self.passwd, self.email, self.reg_dt, self.reg_id)


if __name__ == '__main__':
    m01 = MemberVO('lion', '라이언', '4321', 'kimjmini1122@gmail.com', reg_dt=None, reg_id=None)
    # m01 = MemberVO('lion', '라이언', '4321', 'kimjmini1122@gmail.com', '', 'lion')
    print(m01)

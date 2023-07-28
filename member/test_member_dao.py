import unittest
from member_dao import MemberDao
from member_vo import MemberVO
import common.pcwk_logging as p_log


class TestMemberDao(unittest.TestCase):
    '''MemberDao CRUD 테스트'''

    def setUp(self):
        self.member_dao = MemberDao()
        self.m01 = MemberVO('lion_01', '라이언01', '4321', 'lion_01@gmail.com', '', 'lion_01')
        self.m02 = MemberVO('lion_02', '라이언02', '4321', 'lion_02@gmail.com', '', 'lion_02')
        self.m03 = MemberVO('lion_03', '라이언03', '4321', 'lion_03@gmail.com', '', 'lion_03')

    def test_do_retrieve(self):
        self.member_dao.do_retrieve()

    def ctest_do_update(self):
        # 삭제
        self.member_dao.do_delete(self.m01)
        self.member_dao.do_delete(self.m02)
        self.member_dao.do_delete(self.m03)

        # 등록
        self.member_dao.do_save(self.m01)

        # 조회
        mVO1 = self.member_dao.do_select_one(self.m01)

        # 조회 데이터 수정
        up_str = '_U'

        mVO1.name += up_str
        mVO1.passwd += up_str
        mVO1.email += up_str
        mVO1.reg_id += up_str

        # 수정 데이터로 업데이트
        self.member_dao.do_update(mVO1)

        # 조회
        mVS01 = self.member_dao.do_select_one(mVO1)

        # 수정된 데이터 vs 조회 데이터
        self.is_same_data(mVO1, mVS01)

    '''삭제, 등록, 조회'''

    def ctest_add_and_get(self):
        # 삭제
        self.member_dao.do_delete(self.m01)
        self.member_dao.do_delete(self.m02)
        self.member_dao.do_delete(self.m03)

        # 등록
        self.member_dao.do_save(self.m01)
        self.member_dao.do_save(self.m02)
        self.member_dao.do_save(self.m03)

        # 조회
        outVO1 = self.member_dao.do_select_one(self.m01)
        self.is_same_data(outVO1, self.m01)
        outVO2 = self.member_dao.do_select_one(self.m02)
        self.is_same_data(outVO2, self.m02)
        outVO3 = self.member_dao.do_select_one(self.m03)
        self.is_same_data(outVO3, self.m03)

    def ctest_do_select_one(self):
        outVO1 = self.member_dao.do_select_one(self.m01)
        p_log.logger2.debug('7. outVO1: {}'.format(outVO1))
        self.assertIsNotNone(outVO1)
        self.is_same_data(outVO1, self.m01)

    def ctest_do_delete(self):
        flag = self.member_dao.do_delete(self.m01)
        p_log.logger2.debug('7. test_do_delete flag: {}'.format(flag))
        self.assertEqual(flag, 1)

    def ctest_do_save(self):  # test로 시작하지 않으면 일반 method
        flag = self.member_dao.do_save(self.m01)
        p_log.logger2.debug('7. test_do_save flag: {}'.format(flag))
        self.assertEqual(flag, 1)

    def is_same_data(self, org: MemberVO, vs: MemberVO):
        self.assertEqual(org.user_id, vs.user_id)
        self.assertEqual(org.name, vs.name)
        self.assertEqual(org.passwd, vs.passwd)
        self.assertEqual(org.email, vs.email)
        self.assertEqual(org.reg_id, vs.reg_id)


if __name__ == '__main__':
    unittest.main()
